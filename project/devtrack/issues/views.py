import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Reporter, Issue, CriticalIssue, LowPriorityIssue

REPORTERS_FILE = 'reporters.json'
ISSUES_FILE = 'issues.json'


def _load_data(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            json.dump([], f)
        return []
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def _save_data(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

@csrf_exempt
def reporters_view(request):
    if request.method == 'POST':
        try:
            payload = json.loads(request.body.decode('utf-8'))
        except (ValueError, TypeError, json.JSONDecodeError):
            return JsonResponse({'error': 'Invalid JSON body'}, status=400)

        reporter = Reporter(
            id=payload.get('id'),
            name=payload.get('name'),
            email=payload.get('email'),
            team=payload.get('team')
        )

        try:
            reporter.validate()
        except ValueError as err:
            return JsonResponse({'error': str(err)}, status=400)

        reporters = _load_data(REPORTERS_FILE)

        if any(r.get('id') == reporter.id for r in reporters):
            return JsonResponse({'error': f'Reporter with ID {reporter.id} already exists'}, status=400)

        record = reporter.to_dict()
        reporters.append(record)
        _save_data(REPORTERS_FILE, reporters)
        return JsonResponse(record, status=201)

    elif request.method == 'GET':
        reporters = _load_data(REPORTERS_FILE)
        reporter_id = request.GET.get('id')

        if reporter_id is not None:
            try:
                target_id = int(reporter_id)
            except ValueError:
                return JsonResponse({'error': 'Query param id must be an integer'}, status=400)

            for rep in reporters:
                if rep.get('id') == target_id:
                    return JsonResponse(rep, status=200)
            return JsonResponse({'error': 'Reporter not found'}, status=404)

        return JsonResponse(reporters, safe=False, status=200)

    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def issues_view(request):
    if request.method == 'POST':
        try:
            payload = json.loads(request.body.decode('utf-8'))
        except (ValueError, TypeError, json.JSONDecodeError):
            return JsonResponse({'error': 'Invalid JSON body'}, status=400)

        priority = payload.get('priority')
        params = {
            'id': payload.get('id'),
            'title': payload.get('title'),
            'description': payload.get('description'),
            'status': payload.get('status'),
            'priority': priority,
            'reporter_id': payload.get('reporter_id'),
            'created_at': payload.get('created_at')
        }

        # Subclass factory selection
        if priority == 'critical':
            issue = CriticalIssue(**params)
        elif priority == 'low':
            issue = LowPriorityIssue(**params)
        else:
            issue = Issue(**params)

        try:
            issue.validate()
        except ValueError as err:
            return JsonResponse({'error': str(err)}, status=400)

        issues = _load_data(ISSUES_FILE)

        if any(i.get('id') == issue.id for i in issues):
            return JsonResponse({'error': f'Issue with ID {issue.id} already exists'}, status=400)

        issue_dict = issue.to_dict()
        issues.append(issue_dict)
        _save_data(ISSUES_FILE, issues)

        response_data = dict(issue_dict)
        response_data['message'] = issue.describe()
        return JsonResponse(response_data, status=201)

    elif request.method == 'GET':
        issues = _load_data(ISSUES_FILE)
        issue_id = request.GET.get('id')
        status = request.GET.get('status')

        if issue_id is not None:
            try:
                target_id = int(issue_id)
            except ValueError:
                return JsonResponse({'error': 'Query param id must be an integer'}, status=400)

            for iss in issues:
                if iss.get('id') == target_id:
                    return JsonResponse(iss, status=200)
            return JsonResponse({'error': 'Issue not found'}, status=404)

        if status is not None:
            filtered = [iss for iss in issues if iss.get('status') == status]
            return JsonResponse(filtered, safe=False, status=200)

        return JsonResponse(issues, safe=False, status=200)

    return JsonResponse({'error': 'Method not allowed'}, status=405)