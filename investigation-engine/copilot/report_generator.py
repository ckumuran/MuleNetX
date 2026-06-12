from investigation_engine.copilot.context_builder import (
    get_account_context
)

from investigation_engine.copilot.prompt_builder import (
    build_prompt
)

from investigation_engine.copilot.ollama_client import (
    generate
)


def generate_report(account_id: str):

    context = get_account_context(
        account_id
    )

    if not context:
        return {
            "error": "Account not found"
        }

    prompt = build_prompt(
        context
    )

    report = generate(
        prompt
    )

    return {
        "account": account_id,
        "context": context,
        "report": report
    }
