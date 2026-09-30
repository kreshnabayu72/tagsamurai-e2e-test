---
id: TC-GS-USER-E2E-108-custom-field-placeholder
title: 'Placeholder Custom Field di form User: bawaan dan kustom'
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-515
  - TC-GS-USER-516
  - TC-GS-USER-517
  - TC-GS-USER-518
  - TC-GS-USER-519
  - TC-GS-USER-520
  - TC-GS-USER-521
  - TC-GS-USER-522
  - TC-GS-USER-523
  - TC-GS-USER-524
  - TC-GS-USER-525
  - TC-GS-USER-526
coverage:
  web: automated
---

# Placeholder Custom Field di form User: bawaan dan kustom

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Definisi Custom Field mock tanpa placeholder: `Tax Number` (Text), `Notes` (Text Area), `Grade` (Dropdown), `Birth Date` (Date), `Salary` (Numeric), `Phone` (Phone)
- Definisi Custom Field mock dengan placeholder kustom: `Tax ID` "Enter 16-digit NPWP" (Text), `Job Description Notes` "Enter detailed job responsibilities" (Text Area), `Work Shift` "Choose assigned working shift" (Dropdown), `Certification Expiry` "Select certificate expiry date" (Date), `Annual Target` "Enter target amount without symbols" (Numeric), `Alternate Phone` "Enter alternate emergency phone number" (Phone)

## Test Steps

### Placeholder bawaan

1. Klik `[+ User]` dan amati field tanpa placeholder kustom
2. Verifikasi placeholder bawaan: `Tax Number` "Enter tax number", `Notes` "Enter notes", `Grade` "Select grade", `Birth Date` "Select date", `Salary` "Enter salary", dan sub-input Number `Phone` "Enter phone number"

### Placeholder kustom

3. Amati field yang admin isi placeholder-nya
4. Verifikasi tiap field menampilkan placeholder kustom verbatim seperti di prasyarat

## Notes

- Sumber `user.md` bagian 4.4 dan `custom-field-user/PRD/custom-field-user.md` bagian 5.2b.
