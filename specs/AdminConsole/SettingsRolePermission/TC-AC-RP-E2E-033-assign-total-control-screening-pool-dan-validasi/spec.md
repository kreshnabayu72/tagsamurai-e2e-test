---
id: TC-AC-RP-E2E-033-assign-total-control-screening-pool-dan-validasi
title: "Assign Total Control: Screening Popup, Pool Kandidat, Validasi Diblokir, Cancel, dan Escape"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-120
  - TC-AC-RP-121
  - TC-AC-RP-128
  - TC-AC-RP-129
  - TC-AC-RP-130
coverage:
  web: automated
---

# Assign Total Control: Screening Popup, Pool Kandidat, Validasi Diblokir, Cancel, dan Escape

## Prerequisites

- Mode: FE+BE (backend nyata; spec ini tidak menyimpan perubahan)
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (`Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal: `Default Group`, `Region A` dengan anak `Branch 1`, `Region Jawa` dengan anak `Jakarta` dan `Surabaya`, `Sumatera`), #12 (user Standard), #13 (pemegang Total Control dan Read Only), #14 (penugasan Group Manager), #15 (penugasan peran individual), dan #17 (approver dan toggle). Target aksi memakai user Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini.
- Spec ini tidak mengubah data Pre-setup; tidak ada state yang perlu dipulihkan.
- Kemampuan memantau request jaringan halaman (untuk TC-AC-RP-130: tidak ada request Assign Total Control yang dikirim) disediakan tim FE.
- Suite berjalan serial (`parallel: false`) karena spec mengubah state Pre-setup bersama.
- Env var `AC_RP_TC_PASSWORD` dipakai langkah login hook `before`; nama ini perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-120: Screening popup Assign Total Control

1. Klik tombol "+ Assign"
2. Susuri popup Table User Picker dari atas ke bawah
3. Verifikasi popup tampil sebagai Modal Dialog ukuran `lg`
4. Verifikasi header popup "Assign Total Control"
5. Verifikasi toolbar memuat Search dengan placeholder "Search..."
6. Verifikasi toolbar memuat Filter
7. Verifikasi tabel memuat kolom Checkbox (header Select All), Name, Email, Position, Division, dan Status
8. Verifikasi baris tabel berurut Name A-Z
9. Verifikasi Pagination default 10 baris per halaman
10. Verifikasi footer memuat tombol `[Cancel]` (text, contrast)
11. Verifikasi footer memuat tombol `[Assign]` (primary, enabled walau 0 terpilih)

### TC-AC-RP-121: Pool Assign Total Control menerima status apa pun dan mengecualikan TC, Default User, dan aktor

12. Telusuri seluruh halaman Pagination popup dan amati seluruh baris kandidat
13. Verifikasi kandidat memuat `Dewi Anggraini` (Read Only), `Fajar Nugroho` (Group Manager), `Lisa Wong` (Read Only, Inactive), dan `Maya Putri` (Pending Activation)
14. Verifikasi kandidat memuat user Standard berstatus apa pun: `Alex Tan`, `Dewi Anggreni`, `Hendra Wijaya`, `Indra Kusuma`, `John Dohan`, `Rudi Hartono`, `Sarah Kimura`, `Agus Salim`, `Yuni Lestari` (Pending Email Confirmation), serta `Teguh Santoso` dan `Jane Smith` (Inactive)
15. Verifikasi kandidat tidak memuat pemegang Total Control (`Budi Santoso`, `John Doe`, `Rina Wijaya`, `Sarah Kim`), Default User `Bambang Hartono`, maupun aktor `Siti Nurhaliza`
16. Verifikasi kolom Status picker bernilai `Active` atau `Inactive`
17. Verifikasi Status tidak menyaring kandidat

### TC-AC-RP-130: Assign Total Control tanpa memilih user

18. Klik `[Assign]` tanpa mencentang user
19. Verifikasi inline alert rata kanan di atas footer "You must pick a user" (`severity="danger"`)
20. Verifikasi popup tetap terbuka
21. Verifikasi tidak ada request tersimpan

### TC-AC-RP-128: Cancel popup Assign Total Control tidak menyimpan perubahan

22. Ketik Search `Alex Tan`, tekan Enter
23. Centang `Alex Tan`
24. Klik `[Cancel]`
25. Verifikasi popup tertutup
26. Verifikasi tidak ada toast
27. Verifikasi Tab Total Control tetap 6 baris

### TC-AC-RP-129: Escape menutup popup Assign tanpa menyimpan

28. Klik tombol "+ Assign"
29. Ketik Search `Alex Tan`, tekan Enter
30. Centang `Alex Tan`
31. Tekan Escape
32. Verifikasi popup tertutup
33. Verifikasi dialog Unsaved Changes tidak tampil
34. Verifikasi Tab Total Control tetap 6 baris tanpa baris `Alex Tan`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 12 (tanpa `Verifikasi`; menyiapkan, membersihkan, atau memulihkan state).
- Search untuk menemukan baris target (langkah penghubung, R-16): langkah 22, 29.
- Penyimpangan urutan (S-05, S-10): TC-AC-RP-130 (validasi diblokir) diletakkan sebelum TC-AC-RP-128 dan TC-AC-RP-129 (penutupan popup); popup yang dibuka di langkah 1 dipakai bersama TC-AC-RP-120, 121, dan 130, lalu ditutup di langkah 24.
- Tab Total Control berisi 6 baris sesuai Pre-setup #13 (`Bambang Hartono`, `Budi Santoso`, `John Doe`, `Rina Wijaya`, `Sarah Kim`, `Siti Nurhaliza`).
- Temuan untuk QA:
  - Picker memuat lebih dari 10 kandidat (Pagination default 10) dan TC tidak menyatakan cara menelusuri halaman; spec menelusuri seluruh halaman Pagination untuk asersi daftar kandidat dan memakai Search untuk menemukan baris target (S-14, S-15).
  - TC-AC-RP-130 Expected "tidak ada request tersimpan" tidak memberi cara cek; spec memakai pemantauan request jaringan yang disediakan tim FE tanpa mengarang endpoint (S-11, S-13).
  - TC-AC-RP-121 Expected c "Status tidak menyaring kandidat" tidak punya elemen UI terpisah; diasersi dari daftar kandidat berstatus Pending dan Inactive pada langkah 14.
