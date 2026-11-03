---
id: TC-FA-SU-E2E-036-bulk-tanpa-baris-eligible-dialog-blok-collapse-ke-dialog-single-dan-cancel-bulk
title: "Bulk Tanpa Baris Eligible: Dialog Blok, Collapse ke Dialog Single, dan Cancel Bulk Activate"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-112
  - TC-FA-SU-113
  - TC-FA-SU-114
  - TC-FA-SU-115
  - TC-FA-SU-1049
coverage:
  web: automated
---

# Bulk Tanpa Baris Eligible: Dialog Blok, Collapse ke Dialog Single, dan Cancel Bulk Activate

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Lina Marlina`), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip `seen`, sesi API aktor, pemulihan) mengikuti `suite.md`. Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Client `FaUserMain` (#20) dan Global Settings (#38: pengguna nonaktif di Global Settings; pola varian Dialog Blok). Target memakai pengguna milik spec (S-06).
- Pengguna milik spec (seed API di hook `before`, dihapus di hook `after`; dirujuk lewat `Fixture.fa-settings-user.<kunci>`, fixture belum ada dan disediakan tim FE). Semua bernama `<alias> {runId}-036`, email `<alias>+{runId}-036@qwertysystem.net`; seluruh 10 pengguna tampil pada satu halaman saat Search `{runId}-036`:
  - TC-FA-SU-112: `Rudi Hartono U112` dan `Vina Maharani U112`, keduanya Active dan nonaktif di Global Settings.
  - TC-FA-SU-113: `Doni Prasetyo U113` dan `Fajar Nugroho U113`, keduanya Inactive dan nonaktif di Global Settings.
  - TC-FA-SU-114: `Rudi Hartono U114` (Active, nonaktif di Global Settings) dan `Doni Prasetyo U114` (Inactive, nonaktif di Global Settings).
  - TC-FA-SU-115: `Gita Permata U115` (Active) dan `Doni Prasetyo U115` (Inactive), keduanya aktif di Global Settings.
  - TC-FA-SU-1049: `Doni Prasetyo U1049` dan `Fajar Nugroho U1049`, keduanya Inactive dan aktif di Global Settings.
- Kemampuan teknis: Principal Automation (Pre-setup #12) menonaktifkan pengguna milik spec di Global Settings sebelum spec dan memulihkannya di hook `after` (kemampuan "disediakan tim FE", S-13); pencatat request jaringan Spectra untuk memastikan tidak ada request bulk yang terkirim; kemampuan baca log (disediakan tim FE/BE, tanpa endpoint karangan): hook `before` mencatat baseline jumlah entri tiap pengguna pada Tab Changelog target serta total entri Tab System Log aktor dan Activity Log.
- State global: status pengguna di Global Settings (dipulihkan di `after`); suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-112: Bulk Deactivate tanpa baris eligible

1. Ketik Search `{runId}-036`, tekan Enter
2. Centang `Rudi Hartono U112 {runId}-036` dan `Vina Maharani U112 {runId}-036`
3. Klik Bulk Action > `[Deactivate]`
4. Verifikasi dialog Title `Cannot Deactivate Users` tanpa tanda tanya dengan Body `None of the selected users can be deactivated (already inactive, inactive in Global Settings, or no permission):`, bullet kedua nama, dan tombol tunggal `[OK]`
5. Verifikasi tidak ada request bulk yang terkirim ke server
6. Verifikasi tidak ada toast
7. Klik `[OK]`
8. Verifikasi dialog tertutup
9. Verifikasi seleksi dan Bulk Actions Bar tetap ada

### TC-FA-SU-113: Bulk Activate tanpa baris eligible

10. Klik `[Unselect All]`
11. Centang `Doni Prasetyo U113 {runId}-036` dan `Fajar Nugroho U113 {runId}-036`
12. Klik Bulk Action > `[Activate]`
13. Verifikasi dialog Title `Cannot Activate Users` dengan Body `None of the selected users can be activated (already active, inactive in Global Settings, or no permission):`, bullet kedua nama, dan tombol `[OK]`
14. Verifikasi tidak ada request bulk yang terkirim ke server
15. Verifikasi tidak ada toast
16. Klik `[OK]`
17. Verifikasi seleksi dan Bulk Actions Bar tetap ada

### TC-FA-SU-114: Dialog Blok seleksi satu baris

18. Klik `[Unselect All]`
19. Centang `Rudi Hartono U114 {runId}-036`
20. Klik Bulk Action > `[Deactivate]`
21. Verifikasi dialog Title `Cannot Deactivate User` dengan Body `This user cannot be deactivated (inactive in Global Settings or no permission):` dan satu bullet
22. Klik `[OK]`
23. Klik `[Unselect All]`
24. Centang `Doni Prasetyo U114 {runId}-036`
25. Klik Bulk Action > `[Activate]`
26. Verifikasi dialog Title `Cannot Activate User` dengan Body `This user cannot be activated (inactive in Global Settings or no permission):` dan satu bullet
27. Klik `[OK]`

### TC-FA-SU-115: Bulk dengan satu baris eligible collapse ke dialog Single

28. Klik `[Unselect All]`
29. Centang `Gita Permata U115 {runId}-036` (Active)
30. Klik Bulk Action > `[Deactivate]`
31. Verifikasi dialog identik dengan dialog baris `Deactivate User`: title singular, tanpa daftar bullet bulk, dengan penutup `Are you sure you want to deactivate it?`
32. Klik `[Cancel]`
33. Klik `[Unselect All]`
34. Centang `Doni Prasetyo U115 {runId}-036` (Inactive)
35. Klik Bulk Action > `[Activate]`
36. Verifikasi dialog identik dengan dialog baris `Activate User`
37. Klik `[Cancel]`
38. Klik `[Unselect All]`
39. Centang `Gita Permata U115 {runId}-036` (Active) dan `Doni Prasetyo U115 {runId}-036` (Inactive)
40. Klik Bulk Action > `[Deactivate]`
41. Verifikasi dialog memakai varian Seleksi Campuran, bukan dialog Single
42. Klik `[Cancel]`

### TC-FA-SU-1049: Cancel dialog Bulk Activate

43. Klik `[Unselect All]`
44. Centang `Doni Prasetyo U1049 {runId}-036` dan `Fajar Nugroho U1049 {runId}-036`
45. Klik Bulk Action > `[Activate]`
46. Klik `[Cancel]`
47. Verifikasi dialog `Activate Users` tertutup
48. Verifikasi sakelar Active kedua baris tetap OFF
49. Verifikasi seleksi dan Bulk Actions Bar dipertahankan
50. Verifikasi tidak ada toast
51. Verifikasi jumlah entri Tab Changelog kedua pengguna, total entri Tab System Log aktor, dan total entri Activity Log sama dengan baseline

## Notes

- Alasan di atas 35 langkah (51): semua blok satu topik (dialog bulk tanpa baris eligible atau dengan satu baris eligible, tanpa aksi tulis) dan satu kelas harness (fungsional); tiap blok memakai pengguna milik spec sendiri dan seleksi dibersihkan antar blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16), langkah 7, 16, 22, dan 27 (menutup Dialog Blok), langkah 32, 37, dan 42 (menutup dialog yang hanya dibaca), dan langkah 10, 18, 23, 28, 33, 38, dan 43 (membersihkan seleksi, S-09).
- Klausa "tanpa log" TC-FA-SU-1049 dan klausa "request tidak dikirim" TC-FA-SU-112 diasersi sebagai jumlah terhadap baseline dan pencatat request, bukan spec absence; anchor-nya baseline hook `before` dan dialog yang diasersi.
- Pembagian TC lintas spec: TC-FA-SU-109, TC-FA-SU-110, dan TC-FA-SU-111 ada di spec 035; TC-FA-SU-117 (Dialog Blok pada seleksi satu baris nonaktif di Global Settings) ada di spec 040.
- Temuan untuk QA:
  - TC-FA-SU-112 mencantumkan Vina Maharani sebagai target, padahal Pre-setup #10 memakai nama itu untuk akun aktor "Peran tanpa akses"; spec memakai pengguna milik spec bernama `Vina Maharani U112 {runId}-036` yang dinonaktifkan di Global Settings.
  - TC-FA-SU-113 menyebut "Doni Prasetyo dan Fajar Nugroho (keduanya Inactive, nonaktif di Global Settings varian #38)" sedangkan Pre-setup #38 hanya menyebut Rudi Hartono nonaktif di Global Settings dan varian Dialog Blok untuk Vina, Doni, dan Fajar yang dinonaktifkan Principal Automation; spec mengikuti varian itu.
  - Post Condition TC-FA-SU-112 butir a dan TC-FA-SU-113 butir a (status tidak berubah) tidak punya langkah observasi di TC dan tidak diasersi; butir b diasersi lewat Expected padanan.
  - TC-FA-SU-115 tidak menyatakan Expected untuk keadaan seleksi sebelum aksi; hanya dialog yang diasersi.
  - Target TC adalah pengguna Pre-setup bersama; spec memakai pengguna milik spec dengan suffix (S-06).
