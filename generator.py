def generate_commit(change):
    text = change.lower()

    if any(word in text for word in ["fix", "bug", "error", "issue"]):
        commit_type = "fix"
    elif any(word in text for word in ["add", "create", "new"]):
        commit_type = "feat"
    elif any(word in text for word in ["readme", "documentation", "docs"]):
        commit_type = "docs"
    elif any(word in text for word in ["test", "testing"]):
        commit_type = "test"
    elif any(word in text for word in ["style", "format", "css"]):
        commit_type = "style"
    else:
        commit_type = "chore"

    message = change.strip().rstrip(".")
    return f"{commit_type}: {message}"
