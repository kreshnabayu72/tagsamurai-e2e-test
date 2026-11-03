---
id: TC-GS-NLU-E2E-040-popup-select-user-setup-column-bagian-2-pin-reset
title: "Popup Select User: Setup Column bagian 2 (persisten, Pin, Reset)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-123
  - TC-GS-NLU-126
  - TC-GS-NLU-127
coverage:
  web: automated
---

# Popup Select User: Setup Column bagian 2 (persisten, Pin, Reset)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/nonLoginUser.json` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): pool Login User Represented By No. 10 (semua Active). Spec tidak membuat, mengubah, atau menghapus data backend; Popup Create tidak pernah di-Submit.
- State global: konfigurasi kolom Setup Column Popup Select User disimpan di browser. Hook `after` memulihkannya dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE dan dinyatakan di `suite.md`.

## Test Steps

1. Klik `[+ Non-Login User]` sehingga Popup Create Non-Login User terbuka
2. Klik `[+ Select User]` pada field Represented By sehingga Popup Select User terbuka

### TC-GS-NLU-123: Ceklis kolom Hideable lalu Save pada Setup Column Popup Select User persisten setelah refresh

3. Klik ikon `⋯` pada header kolom Actions > `Setup Column...`
4. Hapus centang Email, Position, Division, dan Status
5. Centang kembali Email lalu hapus centang Name
6. Verifikasi preview tabel mengikuti perubahan sebelum Save
7. Klik `[Save]`
8. Verifikasi kolom Position, Division, Status, dan Name hilang dan hanya Email tersisa
9. Muat ulang halaman, buka Popup Create Non-Login User lalu Popup Select User
10. Verifikasi pengaturan kolom tetap setelah muat ulang (hanya Email tersisa)

### TC-GS-NLU-126: Pin dan Unpin kolom pada Setup Column Popup Select User

11. Klik ikon `⋯` pada header kolom Actions > `Setup Column...`
12. Klik `[Reset to Default]` tanpa menyimpan
13. Pin kolom Name
14. Klik `[Save]`
15. Scroll tabel horizontal
16. Verifikasi kolom Name membeku saat scroll horizontal
17. Klik ikon `⋯` pada header kolom Actions > `Setup Column...`
18. Unpin kolom Name
19. Klik `[Save]`
20. Verifikasi kolom Name ikut bergeser saat scroll horizontal

### TC-GS-NLU-127: Reset to Default mengembalikan Setup Column Popup Select User

21. Klik ikon `⋯` pada header kolom Actions > `Setup Column...`
22. Ubah visibilitas dan urutan kolom
23. Klik `[Reset to Default]`
24. Verifikasi preview kembali ke default (Name, Email, Position, Division, Status visible; kolom curated hidden)
25. Klik `[Save]`
26. Verifikasi tabel mengikuti default
27. Muat ulang halaman, buka Popup Create Non-Login User lalu Popup Select User
28. Verifikasi tabel tetap mengikuti default setelah muat ulang
29. Klik `[Cancel]`
30. Klik `✕` pada Popup Create Non-Login User

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- TC-GS-NLU-121, TC-GS-NLU-122, TC-GS-NLU-124, dan TC-GS-NLU-125 ada di spec 039; TC-GS-NLU-128 sampai TC-GS-NLU-130 ada di spec 129.
- Langkah penghubung tanpa `Verifikasi`: langkah 9 dan 27 (muat ulang halaman dan membuka kembali popup untuk asersi persisten), langkah 12 (mengembalikan dialog ke default tanpa Save sebagai precondition TC-GS-NLU-126 karena TC-GS-NLU-123 meninggalkan hanya kolom Email), dan langkah 29 sampai 30 (menutup popup; Represented By tidak dipilih sehingga tanpa dialog Unsaved Changes). Muat ulang dilakukan saat Popup Create tidak dirty.
- Temuan untuk QA:
  - TC-GS-NLU-126 langkah 4 ("Scroll tabel horizontal") tidak menyebut kondisi yang membuat tabel dapat di-scroll horizontal; dengan lima kolom default popup bisa jadi tidak meluap. TC tidak menambahkan precondition kolom curated; spec mengikuti langkah TC.
  - TC-GS-NLU-127 langkah 3 ("Ubah visibilitas dan urutan kolom") tidak menyebut kolom atau urutan yang diubah dan tidak ada Expected untuk perubahannya; spec memilih perubahan bebas lalu mengasersi hanya hasil `[Reset to Default]`.
