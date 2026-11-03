---
id: TC-GS-NLU-E2E-037-popup-select-user-filter-panel-dan-filter-multi-select
title: "Popup Select User: Filter Panel dan Filter multi-select"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-115
  - TC-GS-NLU-116
coverage:
  web: automated
---

# Popup Select User: Filter Panel dan Filter multi-select

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/nonLoginUser.json` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): pool Login User Represented By No. 10 (semua Active; Position Manager, Branch Manager, Staff dan Division Operations, Finance, Logistics, Warehouse tersebar di baris), serta Custom Field dasar Blood Type (No. 13, Active) yang memunculkan filter `Blood Type`. Spec tidak membuat, mengubah, atau menghapus data backend; Popup Create tidak pernah di-Submit.
- Data uji: Position `Manager` dan `Staff`; Division `Finance`; Status `Active`.
- State global: tidak ada yang diubah.

## Test Steps

1. Klik `[+ Non-Login User]` sehingga Popup Create Non-Login User terbuka
2. Klik `[+ Select User]` pada field Represented By sehingga Popup Select User terbuka

### TC-GS-NLU-115: Screening Filter Panel Popup Select User

3. Klik icon Filter
4. Verifikasi Filter Panel terbuka di bawah toolbar
5. Verifikasi ikon Filter menjadi gelap
6. Verifikasi field `Position` kosong dengan placeholder `All positions`
7. Verifikasi field `Division` kosong dengan placeholder `All divisions`
8. Verifikasi field `Status` kosong dengan placeholder `All statuses`
9. Verifikasi field `Activation Status` kosong dengan placeholder `All statuses`
10. Verifikasi field `Temporary User` kosong dengan placeholder `All options`
11. Verifikasi field date range `Temporary Until` kosong dengan placeholder `Select date`
12. Verifikasi filter Custom Field `Blood Type` kosong dengan placeholder `All blood types`
13. Verifikasi tombol `[Clear Field]` di kiri dan `[Apply]` di kanan

### TC-GS-NLU-116: Filter dropdown multi-select Position, Division, dan Status pada Popup Select User

14. Verifikasi tabel menampilkan sedikitnya satu baris sebelum Filter diterapkan
15. Klik dropdown Position
16. Verifikasi opsi dropdown Position hanya memuat nilai Position yang ada di tabel
17. Pilih Position `Manager` dan `Staff`, klik `[Apply]`
18. Verifikasi seluruh baris hasil memiliki Position Manager atau Staff (logika OR dalam field)
19. Verifikasi ikon Filter menampilkan titik indikator selama ada filter ter-Apply
20. Klik dropdown Division
21. Verifikasi opsi dropdown Division hanya memuat nilai Division yang ada di tabel
22. Pilih Division `Finance`, klik `[Apply]`
23. Verifikasi seluruh baris hasil adalah irisan Position (Manager atau Staff) dan Division Finance
24. Klik dropdown Status
25. Verifikasi opsi dropdown Status hanya memuat nilai Status yang ada di tabel
26. Pilih Status `Active`, klik `[Apply]`
27. Verifikasi seluruh baris hasil sebelumnya tetap tampil (pool hanya berisi Active)
28. Klik `[Clear Field]`
29. Klik `[Apply]`
30. Verifikasi tabel kembali penuh
31. Klik `[Cancel]`
32. Klik `✕` pada Popup Create Non-Login User

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber dipertahankan.
- Langkah penghubung tanpa `Verifikasi`: langkah 31 sampai 32 (menutup popup; Represented By tidak dipilih sehingga tanpa dialog Unsaved Changes).
- TC-GS-NLU-117 (Filter Temporary User, Activation Status, Temporary Until) ada di spec 038.
- Temuan untuk QA: tidak ada.
