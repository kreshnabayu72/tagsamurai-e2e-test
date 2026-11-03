---
id: TC-GS-USER-E2E-172-detail-responsibilities-kolom-pending-tasks-dan-badge-brand-model-type
title: "User Detail Responsibilities: Kolom Group Badge, PIC Kosong, dan Total Asset Kosong pada Pending Tasks, serta Badge Brand dan Model / Type dengan Filter Model / Type pada Borrowed dan Assigned Assets"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-1137
  - TC-GS-USER-1138
coverage:
  web: automated
---

# User Detail Responsibilities: Kolom Group Badge, PIC Kosong, dan Total Asset Kosong pada Pending Tasks, serta Badge Brand dan Model / Type dengan Filter Model / Type pada Borrowed dan Assigned Assets

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10 sampai 22) tidak dipakai sebagai target dan tidak diubah (S-06).
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user dan data Responsibilities FAMS disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD), dihapus di hook `after`:
  - `Ahmad Fauzi {runId}-172`, email `ahmadfauzi+{runId}-172@qwertysystem.net`, Activated, Division `Finance`, Access `Fixed Asset`, dengan:
    - Pending Tasks: satu task dengan Group `General Affairs > Finance`; satu task tanpa Group, tanpa PIC, dan tanpa Total Asset (seeding Group, PIC, dan Total Asset kosong disediakan tim FE/BE).
    - Borrowed Assets: sedikitnya dua baris dengan Model / Type berbeda, yaitu `Latitude 5420` dan `ThinkPad T14`.
    - Assigned Assets: sedikitnya dua baris dengan Model / Type berbeda, yaitu `Latitude 5420` dan `ThinkPad T14`.
  - `ThinkPad T14` adalah nilai pembanding pilihan spec (TC hanya menyebut `Latitude 5420`) supaya Filter Model / Type punya sedikitnya dua nilai distinct (S-11).
- Kemampuan teknis: hover pada Badge Group; membaca tipe tampilan sel (Badge) kolom Brand dan Model / Type; membaca daftar opsi dropdown Model / Type.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus user seed dan data Responsibilities-nya lewat API.

## Test Steps

### Persiapan

1. Ketik Search `Ahmad Fauzi {runId}-172`, tekan Enter
2. Klik Name `Ahmad Fauzi {runId}-172` di User List
3. Klik Tab `Responsibilities`
4. Klik sub-tab `Pending Tasks`

### TC-GS-USER-1137: Kolom Pending Tasks, Group Badge dengan hover hierarki, PIC kosong `—`, Total Asset kosong `0`

5. Verifikasi Group pada task bergrup tampil sebagai Badge
6. Hover Badge Group pada task bergrup
7. Verifikasi hover menampilkan hierarki lengkap `General Affairs > Finance`
8. Verifikasi Group kosong pada task tanpa nilai tampil `—`
9. Verifikasi PIC kosong pada task tanpa nilai tampil `—`
10. Verifikasi Total Asset kosong pada task tanpa nilai tampil `0` (angka bulat, tanpa pemisah ribuan)

### TC-GS-USER-1138: Kolom Brand dan Model / Type berupa Badge dengan filter Model / Type

11. Klik sub-tab `Borrowed Assets`
12. Verifikasi kolom Brand tampil sebagai Badge di sub-tab `Borrowed Assets`
13. Verifikasi kolom Model / Type tampil sebagai Badge di sub-tab `Borrowed Assets`
14. Klik icon Filter
15. Verifikasi Filter Panel memuat field `Model / Type` dengan placeholder `All models/types`
16. Verifikasi opsi field `Model / Type` hanya `Latitude 5420` dan `ThinkPad T14` (nilai yang ada di tabel)
17. Pilih Model / Type `Latitude 5420`
18. Klik `[Apply]`
19. Verifikasi sedikitnya satu baris tampil di tabel sub-tab `Borrowed Assets`
20. Verifikasi seluruh baris tabel sub-tab `Borrowed Assets` ber-Model / Type `Latitude 5420`
21. Klik sub-tab `Assigned Assets`
22. Verifikasi kolom Brand tampil sebagai Badge di sub-tab `Assigned Assets`
23. Verifikasi kolom Model / Type tampil sebagai Badge di sub-tab `Assigned Assets`
24. Klik icon Filter
25. Verifikasi Filter Panel memuat field `Model / Type` dengan placeholder `All models/types`
26. Verifikasi opsi field `Model / Type` hanya `Latitude 5420` dan `ThinkPad T14` (nilai yang ada di tabel)
27. Pilih Model / Type `Latitude 5420`
28. Klik `[Apply]`
29. Verifikasi sedikitnya satu baris tampil di tabel sub-tab `Assigned Assets`
30. Verifikasi seluruh baris tabel sub-tab `Assigned Assets` ber-Model / Type `Latitude 5420`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec 30 langkah. Langkah 21 sampai 30 mengulang langkah 11 sampai 20 pada sub-tab `Assigned Assets` sesuai langkah 4 TC-GS-USER-1138 ("Ulangi langkah 1-3 di sub-tab `Assigned Assets`"); langkah 1 TC itu dipenuhi langkah 2 sampai 4 dan 11.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 (Search), 2 sampai 4, 11, dan 21 (membuka Detail, tab, dan sub-tab), 6 (hover pemicu tooltip, bagian 8b butir 5), 14, 17, 18, 24, 27, dan 28 (membuka dan menerapkan Filter, bagian dari langkah TC).
- Asersi universal (langkah 20 dan 30) didahului `Verifikasi` sedikitnya satu baris tampil (langkah 19 dan 29, bagian 8b butir 2). Filter tidak dikosongkan sebelum spec berakhir karena tidak ada TC berikutnya yang bergantung pada tabel penuh.
- Pembagian TC lintas spec: Filter Panel umum sub-tab Borrowed dan Assigned Assets ada di spec 115 dan 121; screening sub-tab Responsibilities ada di spec 065.
- Temuan untuk QA:
  - TC-GS-USER-1137 dan 1138 menyebut `Ahmad Fauzi` Pre-setup dengan task dan aset ber-model `Latitude 5420`; spec memakai seed bersuffix milik spec dengan seeding FAMS yang disediakan tim FE/BE (S-06, S-12). Group, PIC, dan Total Asset kosong tidak ada mekanisme seeding di TC, PRD, atau LLD (Need Confirmation).
  - TC-GS-USER-1137 tidak menyebut kolom Total Asset pada task bergrup; hanya sel task tanpa nilai yang diasersi.
  - TC-GS-USER-1138 Expected b ("opsi hanya nilai yang ada di tabel") tidak menyebut nilai lain; spec men-seed `ThinkPad T14` sebagai pembanding dan mengasersi daftar opsi persis kedua nilai.
