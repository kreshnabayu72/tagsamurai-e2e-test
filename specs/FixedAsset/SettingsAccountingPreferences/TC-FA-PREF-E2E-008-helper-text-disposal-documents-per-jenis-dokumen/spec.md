---
id: TC-FA-PREF-E2E-008-helper-text-disposal-documents-per-jenis-dokumen
title: "Helper Text Disposal Documents per Jenis Dokumen"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-40
  - TC-FA-PREF-41
  - TC-FA-PREF-42
  - TC-FA-PREF-43
  - TC-FA-PREF-44
  - TC-FA-PREF-45
sourceRules: ["DOC-01", "DOC-02", "DOC-03", "DOC-04", "DOC-05", "DOC-06"]
smoke: []
dependsOn: []
trace:
  "DOC-01": [2, 3]
  "DOC-02": [4, 5]
  "DOC-03": [6, 7]
  "DOC-04": [8, 9]
  "DOC-05": [10, 11]
  "DOC-06": [12, 13]
coverage:
  web: automated
---

# Helper Text Disposal Documents per Jenis Dokumen

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup (hanya dibaca, tidak diubah): Preferences nilai awal PA-2, tidak terkunci, semua setting wajib terisi, Disposal Documents keenam jenis (Sell, Scrap, Lost, Donate, Trade-in, Write-off) bernilai "Optional". Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-40: Helper text jenis Sell

1. Gulir ke SectionCard Disposal
2. Verifikasi helper text di bawah Select Disposal Documents jenis Sell: "Example: Receipt"
3. Verifikasi nilai Select jenis Sell tetap "Optional"

### TC-FA-PREF-41: Helper text jenis Scrap

4. Verifikasi helper text di bawah Select Disposal Documents jenis Scrap: "Example: Destruction report"
5. Verifikasi nilai Select jenis Scrap tetap "Optional"

### TC-FA-PREF-42: Helper text jenis Lost

6. Verifikasi helper text di bawah Select Disposal Documents jenis Lost: "Example: Loss report"
7. Verifikasi nilai Select jenis Lost tetap "Optional"

### TC-FA-PREF-43: Helper text jenis Donate

8. Verifikasi helper text di bawah Select Disposal Documents jenis Donate: "Example: Donation letter"
9. Verifikasi nilai Select jenis Donate tetap "Optional"

### TC-FA-PREF-44: Helper text jenis Trade-in

10. Verifikasi helper text di bawah Select Disposal Documents jenis Trade-in: "Example: Trade-in agreement"
11. Verifikasi nilai Select jenis Trade-in tetap "Optional"

### TC-FA-PREF-45: Helper text jenis Write-off

12. Verifikasi helper text di bawah Select Disposal Documents jenis Write-off: "Example: Investigation report"
13. Verifikasi nilai Select jenis Write-off tetap "Optional"

## Notes

- Langkah penghubung (S-03): langkah 1 (gulir ke SectionCard Disposal, satu kali untuk keenam TC karena TC hanya mengamati tanpa submit dan SectionCard tetap pada layar). Layar Preferences dibuka hook `beforeEach` suite, sehingga langkah TC "Buka Tab Preferences" tidak diulang.
- Urutan TC dalam spec: TC-FA-PREF-40 sampai 45 sesuai urutan jenis dokumen. Spec tidak mengubah Preferences; form tidak dirty di akhir spec.
- Temuan untuk QA: tidak ada temuan pada TC sumber spec ini.
