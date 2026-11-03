---
id: TC-FA-SU-E2E-037-bulk-actions-bar-counter-select-all-unselect-all-kondisi-tampil-aksi-dan-seleksi
title: "Bulk Actions Bar: Counter, Select All, Unselect All, Kondisi Tampil Aksi, dan Seleksi Dipertahankan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-120
  - TC-FA-SU-121
  - TC-FA-SU-122
coverage:
  web: automated
---

# Bulk Actions Bar: Counter, Select All, Unselect All, Kondisi Tampil Aksi, dan Seleksi Dipertahankan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Lina Marlina`), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip `seen`, sesi API aktor, pemulihan) mengikuti `suite.md`. Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Client `FaUserMain` (#20, 25 pengguna; Default User dan akun aktor tidak dapat dipilih) dan Global Settings (#38, pola pengguna nonaktif di Global Settings). Target aksi tulis memakai pengguna milik spec (S-06).
- Pengguna milik spec (seed API di hook `before`, dihapus di hook `after`; dirujuk lewat `Fixture.fa-settings-user.<kunci>`, fixture belum ada dan disediakan tim FE). Semua bernama `<alias> {runId}-037`, email `<alias>+{runId}-037@qwertysystem.net`; total 10 pengguna milik spec yang dapat dipilih:
  - TC-FA-SU-121: `Gita Permata U121` dan `Budi Santoso U121` (Active, Activated); `Doni Prasetyo U121` dan `Fajar Nugroho U121` (Inactive); `Hana Kusuma U121` dan `Kartika Sari U121` (Pending Activation).
  - TC-FA-SU-122: `Gita Permata U122` dan `Hana Kusuma U122` (Active); `Rudi Hartono U122` dan `Vina Maharani U122` (Active, nonaktif di Global Settings lewat Principal Automation, kemampuan "disediakan tim FE", dipulihkan di hook `after`).
- Nilai N tombol `Select All (N records)` diturunkan dari seeding (8b butir 10): 25 pengguna Pre-setup dikurangi Default User dan akun aktor (23) ditambah 10 pengguna milik spec, sehingga N = 33.
- Seleksi bertahan lintas halaman (ukuran halaman 10); tidak ada intercept, jam server, atau klien HTTP. State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-120: Counter, Select All, Unselect All, dan persistensi seleksi lintas halaman

1. Centang satu baris pada halaman 1
2. Verifikasi Bulk Actions Bar tampil dengan counter `1 User selected`
3. Centang baris kedua
4. Verifikasi counter `2 Users selected`
5. Verifikasi tombol `Select All (33 records)` tampil dengan N sama dengan jumlah baris yang checkbox-nya dapat dipilih
6. Klik `Select All`
7. Verifikasi label tombol berganti menjadi `[Unselect All]`
8. Pindah ke halaman 2
9. Verifikasi seleksi bertahan pada halaman 2
10. Klik `[Unselect All]`
11. Centang satu baris
12. Klik `[×]` pada Bulk Actions Bar
13. Verifikasi seleksi dibatalkan
14. Verifikasi Bulk Actions Bar hilang

### TC-FA-SU-121: Kondisi tampil tiap aksi mengikuti komposisi status seleksi

15. Ketik Search `U121`, tekan Enter
16. Centang `Gita Permata U121 {runId}-037` dan `Budi Santoso U121 {runId}-037` (Active)
17. Verifikasi `[Activate]` Hidden pada seleksi yang seluruhnya Active
18. Verifikasi `[Edit Home Group]` tampil
19. Klik `[Unselect All]`
20. Centang `Doni Prasetyo U121 {runId}-037` dan `Fajar Nugroho U121 {runId}-037` (Inactive)
21. Verifikasi `[Deactivate]` Hidden pada seleksi yang seluruhnya Inactive
22. Klik `[Unselect All]`
23. Centang `Hana Kusuma U121 {runId}-037` dan `Kartika Sari U121 {runId}-037` (Pending Activation)
24. Verifikasi `[Resend Activation Email]` tampil pada seleksi yang seluruhnya Pending Activation
25. Centang `Gita Permata U121 {runId}-037` (Activated) sehingga seleksi campuran
26. Verifikasi `[Activate]` dan `[Deactivate]` keduanya tampil pada seleksi campuran
27. Verifikasi `[Resend Activation Email]` Hidden pada seleksi campuran status
28. Verifikasi aksi `Resend Confirmation Email` tidak tampil pada Bulk Actions Bar

### TC-FA-SU-122: Seleksi dipertahankan saat dialog dibatalkan dan di-reset setelah aksi ter-commit

29. Klik `[Unselect All]`
30. Ganti isi kotak search dengan `U122`, tekan Enter
31. Centang `Gita Permata U122 {runId}-037` dan `Hana Kusuma U122 {runId}-037` (Active)
32. Klik Bulk Action > `[Deactivate]`
33. Klik `[Cancel]`
34. Verifikasi seleksi dan Bulk Actions Bar dipertahankan
35. Klik Bulk Action > `[Deactivate]`
36. Klik `[Deactivate]` pada dialog
37. Verifikasi seleksi dikosongkan
38. Verifikasi Bulk Actions Bar tersembunyi
39. Centang `Rudi Hartono U122 {runId}-037` dan `Vina Maharani U122 {runId}-037` (nonaktif di Global Settings)
40. Klik Bulk Action > `[Deactivate]`
41. Klik `[OK]` pada Dialog Blok
42. Verifikasi seleksi dan Bulk Actions Bar dipertahankan

## Notes

- Alasan di atas 35 langkah (42): semua blok satu topik (Bulk Actions Bar dan perilaku seleksi) dan satu kelas harness (fungsional); tiap blok memakai seleksi dan pengguna milik spec sendiri dengan seleksi dibersihkan antar blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): langkah 15 (Search untuk menemukan baris target, R-16), langkah 30 (mengganti isi kotak search yang masih berisi `U121`, bagian 8b butir 9), langkah 19, 22, dan 29 (membersihkan seleksi, S-09), dan langkah 33 dan 41 (menutup dialog).
- Pembagian TC lintas spec: TC-FA-SU-124 (Select All oleh aktor Manage global user & role) ada di spec 040; TC-FA-SU-123 (Selection Limit) ada di spec kelas e.
- Temuan untuk QA:
  - TC-FA-SU-120 Expected butir b menulis `Select All (23 records)` dari populasi 25 pengguna Pre-setup; spec menambah 10 pengguna milik spec untuk TC-FA-SU-121 dan TC-FA-SU-122 sehingga N diturunkan menjadi 33 dari seeding.
  - TC-FA-SU-120 Expected butir a menyebut counter `[N] Users selected` untuk lebih dari satu baris; spec mengasersi N = 2 pada langkah 4. Langkah 8 TC (pindah ke halaman 2) memakai asumsi ukuran halaman 10 dan N lebih besar dari 10.
  - TC-FA-SU-121 langkah 3 menyebut Hana Kusuma dan Kartika Sari sebagai "Pending Activation" tanpa status aktif; spec memakai keduanya Active. Langkah 4 menyebut "Gita (Activated)"; spec memakai pengguna Active dengan Activation Status Activated. Expected butir b menyatakan `[Edit Home Group]` tampil pada seleksi 1 baris atau lebih; diasersi pada langkah 18 saja. Expected butir d ("tidak pernah tampil") diasersi pada langkah 28 saja.
  - TC-FA-SU-122 Post Condition menyebut "Gita Permata dan Hana Kusuma Inactive"; sakelar keduanya tidak diasersi karena Expected hanya menyebut seleksi dan bar. Status itu tidak punya langkah observasi di TC.
  - Target TC (Gita Permata, Hana Kusuma, Rudi Hartono, Vina Maharani) adalah pengguna Pre-setup bersama; spec memakai pengguna milik spec dengan suffix (S-06).
