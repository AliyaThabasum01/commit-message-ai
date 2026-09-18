from generator import generate_commit

print("🤖 Commit Message Generator")
print("=" * 40)

change = input("What did you change? ").strip()

if not change:
    print("❌ Please describe your changes.")
else:
    commit = generate_commit(change)

    print("\n✨ Suggested commit:")
    print(commit)
