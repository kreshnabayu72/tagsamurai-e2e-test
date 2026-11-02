---
id: TC-AC-RP-E2E-078-tab-group-manager-sort-dan-setup-column
title: "Tab Group Manager: Sort dan Setup Column"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-267
  - TC-AC-RP-268
  - TC-AC-RP-269
  - TC-AC-RP-270
  - TC-AC-RP-271
coverage:
  web: automated
---

# Tab Group Manager: Sort dan Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD` (nama env baru, perlu didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini: mengikuti pernyataan hook suite di `suite.md`.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role, kolom) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script).
- Spec ini tidak menulis data Pre-setup; tidak ada record bersuffix `+{runId}-NNN` yang dibuat.
- Data Pre-setup Tab Group Manager (Pre-setup #14), tiga baris: `Fajar Nugroho` — `Region Jawa` ("Bambang H" 11 Jun 2026, 10:30), `Fajar Nugroho` — `Sumatera` ("Siti N" 16 Jun 2026, 09:05), `Jane Smith` — `Region Jawa` ("Siti N" 07 Jun 2026, 09:30). Tiap kolom yang diurutkan memiliki sedikitnya dua nilai distinct.
- Custom field User aktif (Pre-setup #12): `Employee Grade` dan `Nickname`.
- Pemulihan Setup Column: preferensi kolom di browser dihapus di hook `after` (kemampuan disediakan tim FE; bukan `[Reset to Default]`).
- Kemampuan teknis: penghapusan preferensi kolom di browser (disediakan tim FE).

## Test Steps

1. Klik tab `Group Manager`

### TC-AC-RP-267: Sort Tab Group Manager kolom Name

2. Klik header Name sekali
3. Verifikasi urutan Name A-Z
4. Klik header Name kedua kali
5. Verifikasi urutan Name Z-A
6. Klik header Name ketiga kali
7. Verifikasi urutan kembali netral ke Name A-Z

### TC-AC-RP-268: Sort Tab Group Manager kolom Group

8. Klik header Group sekali
9. Verifikasi urutan nama group A-Z
10. Klik header Group kedua kali
11. Verifikasi urutan nama group Z-A
12. Klik header Group ketiga kali
13. Verifikasi urutan kembali netral ke Name A-Z

### TC-AC-RP-269: Sort Tab Group Manager kolom Modified By

14. Klik header Modified By sekali
15. Verifikasi urutan Modified By A-Z
16. Klik header Modified By kedua kali
17. Verifikasi urutan Modified By Z-A
18. Klik header Modified By ketiga kali
19. Verifikasi urutan kembali netral ke Name A-Z

### TC-AC-RP-270: Sort Tab Group Manager kolom Last Updated

20. Klik header Last Updated sekali
21. Verifikasi urutan Last Updated Oldest First
22. Klik header Last Updated kedua kali
23. Verifikasi urutan Last Updated Newest First
24. Klik header Last Updated ketiga kali
25. Verifikasi urutan kembali netral ke Name A-Z

### TC-AC-RP-271: Setup Column Tab Group Manager

26. Buka Column Visibility
27. Verifikasi daftar kolom memuat Name, Group, Position, Division, Status, Modified By, dan Last Updated serta kolom curated Email, Activation Status, Temporary User, Temporary Until, TAG, dan Custom Field (`Employee Grade`, `Nickname`)
28. Sembunyikan kolom Group
29. Verifikasi kolom Group tidak tampil di tabel

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec fungsional tanpa kelas harness khusus.
- Langkah 1 membuka Tab Group Manager sekali untuk seluruh TC (langkah "Klik tab `Group Manager`" TC-AC-RP-267 sampai 271 tidak diulang); klik ketiga tiap siklus sort mengembalikan urutan bawaan sehingga TC berikutnya mulai dari keadaan netral (S-09).
- TC-AC-RP-271 dijalankan terakhir karena menyimpan konfigurasi kolom; hook `after` menghapus preferensi kolom.
- Temuan untuk QA: Column Visibility pada TC-AC-RP-271 tidak menyebut `[Save]`; spec mengikuti TC. Daftar "Custom Field" pada Expected TC-AC-RP-271 tidak menyebut nama field; spec memakai `Employee Grade` dan `Nickname` dari Pre-setup #12.
