---
id: TC-FA-SU-E2E-040-bulk-skip-nonaktif-global-settings-skip-tier-dan-select-all-aktor-manage-user-dan-role
title: "Bulk: Skip Nonaktif Global Settings, Skip Tier Total Control dan Read Only, dan Select All oleh Aktor Manage user & role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-116
  - TC-FA-SU-117
  - TC-FA-SU-124
coverage:
  web: automated
---

# Bulk: Skip Nonaktif Global Settings, Skip Tier Total Control dan Read Only, dan Select All oleh Aktor Manage user & role

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Lina Marlina`), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip `seen`, sesi API aktor, pemulihan) mengikuti `suite.md`.
- Akun ganti akun (langkah eksplisit; hook `after` memulihkan sesi ke Total Control default suite):

  | Role yang diuji | Akun | Password |
  |---|---|---|
  | Manage global user & role (Update) | Pre-setup #4, `Qori Akbar`; email tidak tertulis di Pre-setup TC, disediakan tim FE | `Spectra.env.FA_MURG_UPD_PASSWORD` |

  Nama env `FA_MURG_UPD_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Client `FaUserMain` (#20, 25 pengguna), penugasan tier #23 (Lina Marlina Total Control, Citra Lestari Read Only, Ahmad Dahlan Default User; ketiganya dibaca dan di-skip, tidak diubah), dan Global Settings #38 (pola pengguna nonaktif di Global Settings). Target aksi tulis TC-FA-SU-117 dan TC-FA-SU-116 memakai pengguna milik spec (S-06).
- Pengguna milik spec (seed API di hook `before`, dihapus di hook `after`; dirujuk lewat `Fixture.fa-settings-user.<kunci>`, fixture belum ada dan disediakan tim FE). Email `<alias>+{runId}-040@qwertysystem.net` dengan alias huruf kecil:
  - TC-FA-SU-117: `Gita Permata U117 {runId}-040` (Active) dan `Rudi Hartono U117 {runId}-040` (Active, nonaktif di Global Settings lewat Principal Automation, kemampuan "disediakan tim FE", dipulihkan di hook `after`).
  - TC-FA-SU-116: `Gita Permata U116 {runId}-040` (Active).
- Nilai N tombol `Select All (N records)` pada TC-FA-SU-124 diturunkan dari seeding (8b butir 10): 25 pengguna Pre-setup dikurangi Default User dan akun aktor Qori Akbar (23) ditambah 3 pengguna milik spec, sehingga N = 26.
- Kemampuan baca log (disediakan tim FE/BE, tanpa endpoint karangan): hook `before` mencatat baseline jumlah entri ber-Name Lina Marlina, Citra Lestari, dan pengguna milik spec pada Tab Changelog target, Tab System Log aktor, dan Activity Log.
- State global: TC-FA-SU-124 menonaktifkan seluruh pengguna Pre-setup `FaUserMain` yang dapat dipilih kecuali Total Control dan Read Only (skip tier). Hook `after` memulihkan status aktif pengguna Pre-setup ke kondisi Tabel Pre-setup lewat seed API (Catatan TC); spec ini dijalankan sesudah spec lain dan suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-117: Bulk dengan baris nonaktif di Global Settings di-skip

1. Ketik Search `U117`, tekan Enter
2. Centang `Gita Permata U117 {runId}-040` dan `Rudi Hartono U117 {runId}-040`
3. Klik Bulk Action > `[Deactivate]`
4. Verifikasi `Rudi Hartono U117 {runId}-040` (nonaktif di Global Settings) tercantum pada kelompok `The following will be skipped (already inactive, inactive in Global Settings, or no permission):`
5. Klik `[Continue]`
6. Verifikasi sakelar Active `Rudi Hartono U117 {runId}-040` tetap ON (tidak diproses)
7. Verifikasi sakelar Active `Gita Permata U117 {runId}-040` berpindah ke OFF
8. Centang hanya `Rudi Hartono U117 {runId}-040`
9. Klik Bulk Action > `[Deactivate]`
10. Verifikasi Dialog Blok tampil dengan alasan `inactive in Global Settings`
11. Klik `[OK]`

### TC-FA-SU-116: Bulk oleh aktor Manage user & role, target tier di-skip

12. Ganti akun: Logout
13. Login sebagai Qori Akbar (Manage global user & role (Update)) dengan `Spectra.env.FA_MURG_UPD_PASSWORD`
14. Ketik Search `Gita Permata U116 {runId}-040`, tekan Enter
15. Centang `Gita Permata U116 {runId}-040`
16. Ganti isi kotak search dengan `Lina Marlina`, tekan Enter
17. Centang `Lina Marlina`
18. Verifikasi checkbox `Lina Marlina` (Total Control) tercentang
19. Ganti isi kotak search dengan `Citra Lestari`, tekan Enter
20. Centang `Citra Lestari`
21. Verifikasi checkbox `Citra Lestari` (Read Only) tercentang
22. Klik Bulk Action > `[Deactivate]`
23. Verifikasi dialog campuran mencantumkan `Lina Marlina` dan `Citra Lestari` pada kelompok `The following will be skipped (already inactive, inactive in Global Settings, or no permission):`
24. Klik `[Continue]`
25. Verifikasi toast "Success, user has been deactivated. Some items were skipped." tampil
26. Verifikasi sakelar Active `Lina Marlina` dan `Citra Lestari` tetap ON
27. Verifikasi jumlah entri ber-Name `Lina Marlina` dan `Citra Lestari` pada Tab Changelog target, Tab System Log aktor, dan Activity Log sama dengan baseline
28. Klik `(←)` pada kotak Search

### TC-FA-SU-124: Select All oleh aktor Manage user & role

29. Klik `Select All`
30. Verifikasi tombol `Select All (26 records)` menghitung hanya baris yang checkbox-nya dapat dipilih
31. Verifikasi baris `Lina Marlina` (Total Control) dan `Citra Lestari` (Read Only) ikut terpilih
32. Klik Bulk Action > `[Deactivate]`
33. Klik `[Continue]`
34. Verifikasi sakelar Active `Lina Marlina` dan `Citra Lestari` tetap ON (di-skip saat eksekusi Deactivate)

## Notes

- Alasan: spec memuat TC beda akun dengan Step ganti akun eksplisit (bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras). TC-FA-SU-124 ditulis paling akhir karena Bulk Deactivate seluruh baris yang dapat dipilih mengubah pengguna Pre-setup bersama (pemulihan di hook `after`, S-06).
- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16), langkah 11 (menutup Dialog Blok), dan langkah 12 dan 13 (ganti akun, S-07). Langkah 14, 16, dan 19 memilih tiap baris target lewat Search (R-16, bagian 8b butir 9) sebagai pengganti pindah halaman bersyarat; langkah 15, 17, dan 20 adalah Centang dari Langkah Uji TC-FA-SU-116. Langkah 28 menutup input Search dan mereset tabel supaya Select All pada langkah 29 mencakup seluruh baris yang dapat dipilih, bukan hanya hasil Search terakhir; langkah 29 memakai seleksi bersih hasil commit langkah 24.
- Pembagian TC lintas spec: TC-FA-SU-109, TC-FA-SU-110, dan TC-FA-SU-111 (seleksi campuran) ada di spec 035; TC-FA-SU-1065 dan TC-FA-SU-1066 (arah Activate pada tier) tidak masuk spec ini.
- Temuan untuk QA:
  - TC-FA-SU-124 langkah 3 hanya meminta Bulk Action > `[Deactivate]` tanpa menyebut konfirmasi, tetapi Expected butir b menyebut tier "di-skip saat eksekusi"; spec menambahkan klik `[Continue]` pada langkah 33 agar eksekusi terjadi (S-15). Konfirmasi itu menonaktifkan seluruh pengguna Pre-setup yang dapat dipilih selain tier; pemulihan lewat seed API disediakan tim FE/BE.
  - TC-FA-SU-116 Langkah Uji 3 memilih tiga pengguna "pindah halaman bila perlu" tanpa menyebut halaman; spec memilih tiap baris lewat Search dan mengasumsikan seleksi bertahan lintas pergantian Search seperti lintas halaman (TC-FA-SU-120 Expected a); mohon konfirmasi.
  - TC-FA-SU-116 dan TC-FA-SU-124 tidak menyebut email Qori Akbar; nama env password diusulkan.
  - TC-FA-SU-117 Post Condition ("tanpa entri log" untuk Rudi Hartono) tidak punya langkah observasi di TC dan tidak diasersi. TC-FA-SU-116 Post Condition butir tanpa entri log diasersi pada langkah 27 karena identik dengan Expected butir c.
  - TC-FA-SU-117 Expected butir b tidak menulis judul dan isi Dialog Blok; hanya alasan `inactive in Global Settings` yang diasersi (teks lengkap Dialog Blok singular ada di TC-FA-SU-114, spec 036).
  - Target TC (Gita Permata, Rudi Hartono) adalah pengguna Pre-setup bersama; spec memakai pengguna milik spec dengan suffix (S-06). Lina Marlina dan Citra Lestari pada TC-FA-SU-116 dan TC-FA-SU-124 hanya dipilih dan di-skip.
