from niusy.audit.fairness import FairnessAuditor

def main():
    auditor = FairnessAuditor()
    print(f"--- {auditor} Initialized ---")

    # Test Records with Confidence Levels
    # This simulates observations from a neural net (e.g., 'model is 85% sure this is a high score')
    records = [
        {
            "id": "REC-001 (Strong Bias Risk)",
            "is_protected_group": 1.0,
            "is_rejected": 1.0,
            "has_high_score": 0.95,  # Solid Merit, yet rejected
        },
        {
            "id": "REC-002 (Uncertain Merit)",
            "is_protected_group": 1.0,
            "is_rejected": 1.0,
            "has_high_score": 0.6,   # Low confidence in merit -> Low confidence in 'Bias'
        },
        {
            "id": "REC-003 (Inconsistent Only)",
            "is_not_protected": 1.0,
            "is_rejected": 1.0,
            "has_high_score": 0.9,
        }
    ]

    for record in records:
        record_id = record['id']
        # Audit with probabilities
        alerts = auditor.audit_record(record)
        
        if alerts:
            alert_str = ", ".join([f"{name} ({score:.2f} confidence)" for name, score in alerts.items()])
            print(f"\n[ALERT - {record_id}]\n  Reasoning Result: {alert_str}")
        else:
            print(f"\n[OK - {record_id}] No symbolic fairness violations found.")

if __name__ == "__main__":
    main()

