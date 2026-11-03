---
id: TC-FA-SU-E2E-035-bulk-seleksi-campuran-dialog-dua-kelompok-skip-tier-dan-skip-nonaktif-global-settings
title: "Bulk Seleksi Campuran: Dialog Dua Kelompok untuk Deactivate dan Activate serta Peringatan Aset pada Kelompok Deactivated"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-109
  - TC-FA-SU-110
  - TC-FA-SU-111
coverage:
  web: automated
---

# Bulk Seleksi Campuran: Dialog Dua Kelompok untuk Deactivate dan Activate serta Peringatan Aset pada Kelompok Deactivated

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Lina Marlina`), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip `seen`, sesi API aktor, pemulihan) mengikuti `suite.md`. Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Client `FaUserMain` (#20), Responsibilities #24 (pemegang aset aktif) sebagai pola data, dan layanan terkendali (#37: layanan pemeriksaan aset dan approval dapat di-intercept). Target aksi tulis memakai pengguna milik spec (S-06).
- Pengguna milik spec (seed API di hook `before`, dihapus di hook `after`; dirujuk lewat `Fixture.fa-settings-user.<kunci>`, fixture belum ada dan disediakan tim FE). Email `<alias>+{runId}-035@qwertysystem.net` dengan alias huruf kecil:
  - TC-FA-SU-109: `Gita Permata U109 {runId}-035` (Active) dan `Doni Prasetyo U109 {runId}-035` (Inactive).
  - TC-FA-SU-110: `Doni Prasetyo U110 {runId}-035` (Inactive) dan `Gita Permata U110 {runId}-035` (Active).
  - TC-FA-SU-111: `Budi Santoso U111 {runId}-035` (Active, memegang aset aktif) dan `Fajar Nugroho U111 {runId}-035` (Inactive).
- Kemampuan teknis:
  - `Spectra.intercept()` atas respons HTTP di atas backend nyata: respons pemeriksaan aset aktif dan approval tertunda dibuat gagal (TC-FA-SU-111), dilepas segera setelah dialog terbaca (S-09).
  - Seed pemegang aset aktif untuk pengguna milik spec disediakan tim FE/BE.
  - Kemampuan baca log (disediakan tim FE/BE, tanpa endpoint karangan): hook `before` mencatat baseline jumlah entri tiap pengguna milik spec pada Tab Changelog target serta total entri Tab System Log aktor dan Activity Log.
- State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-109: Bulk Deactivate seleksi campuran

1. Ketik Search `U109`, tekan Enter
2. Centang `Gita Permata U109 {runId}-035` (Active) dan `Doni Prasetyo U109 {runId}-035` (Inactive)
3. Klik Bulk Action > `[Deactivate]`
4. Verifikasi dialog Title `Deactivate Users` dengan kelompok `The following will be deactivated:` berisi `• Gita Permata U109 {runId}-035` disusul kalimat dampak logout `These users will be immediately logged out and blocked from entering FAMS.`
5. Verifikasi kelompok `The following will be skipped (already inactive, inactive in Global Settings, or no permission):` berisi `• Doni Prasetyo U109 {runId}-035`, penutup `Are you sure you want to continue?`, serta tombol `[Cancel]` dan `[Continue]`
6. Klik `[Continue]`
7. Verifikasi sakelar Active `Gita Permata U109 {runId}-035` berpindah ke OFF
8. Verifikasi sakelar `Doni Prasetyo U109 {runId}-035` tetap OFF (tidak diproses)
9. Verifikasi toast "Success, user has been deactivated. Some items were skipped." tampil
10. Verifikasi jumlah entri ber-Name `Doni Prasetyo U109 {runId}-035` pada Tab Changelog target, Tab System Log aktor, dan Activity Log sama dengan baseline

### TC-FA-SU-110: Bulk Activate seleksi campuran

11. Ganti isi kotak search dengan `U110`, tekan Enter
12. Centang `Doni Prasetyo U110 {runId}-035` (Inactive) dan `Gita Permata U110 {runId}-035` (Active)
13. Klik Bulk Action > `[Activate]`
14. Verifikasi dialog Title `Activate Users` dengan kelompok `The following will be activated:` berisi `• Doni Prasetyo U110 {runId}-035` dan kelompok `The following will be skipped (already active, inactive in Global Settings, or no permission):` berisi `• Gita Permata U110 {runId}-035`
15. Verifikasi dialog tanpa kalimat dampak dan tanpa peringatan aset atau approval
16. Verifikasi penutup `Are you sure you want to continue?` dengan tombol `[Cancel]` dan `[Continue]` (severity primary)
17. Klik `[Continue]`
18. Verifikasi sakelar Active `Doni Prasetyo U110 {runId}-035` berpindah ke ON
19. Verifikasi toast "Success, user has been activated. Some items were skipped." tampil

### TC-FA-SU-111: Peringatan aset hanya untuk baris kelompok deactivated

20. Ganti isi kotak search dengan `U111`, tekan Enter
21. Centang `Budi Santoso U111 {runId}-035` (Active, memegang aset) dan `Fajar Nugroho U111 {runId}-035` (Inactive)
22. Klik Bulk Action > `[Deactivate]`
23. Verifikasi peringatan pemegang aset hanya mencantumkan `Budi Santoso U111 {runId}-035` (kelompok will be deactivated), bukan baris pada kelompok skipped
24. Klik `[Cancel]`
25. Pasang intercept: respons pemeriksaan aset aktif dan approval tertunda menjadi gagal
26. Klik Bulk Action > `[Deactivate]`
27. Verifikasi satu baris `We couldn't check this user's active assets or pending approvals. You can still continue.` tampil pada varian Deactivate
28. Lepas intercept pemeriksaan aset aktif dan approval tertunda
29. Klik `[Cancel]`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16), langkah 11 dan 20 (mengganti isi kotak search yang masih berisi nilai sebelumnya, bagian 8b butir 9), langkah 24 dan 29 (menutup dialog yang hanya dibaca), dan langkah 28 (melepas intercept, S-09).
- Pembagian TC lintas spec: TC-FA-SU-116 dan TC-FA-SU-117 (skip tier dan skip nonaktif Global Settings) ada di spec 040.
- Temuan untuk QA:
  - TC-FA-SU-109 Expected butir c menyebut Doni "tidak menulis log" dan Post Condition butir b menyebut satu entri hanya untuk Gita; spec mengasersi klausa Expected untuk Doni (langkah 10) sementara entri Gita pada tiga surface tidak punya langkah observasi di TC dan tidak diasersi. Post Condition TC-FA-SU-110 butir a dan b juga tanpa langkah observasi dan tidak diasersi.
  - TC-FA-SU-111 Expected butir b menyebut baris pemeriksaan gagal "di varian Deactivate saja"; TC tidak memberi langkah untuk varian Activate sehingga spec hanya mengasersi bahwa baris tampil pada varian Deactivate. Pre-setup #37 dipakai lewat intercept respons pemeriksaan.
  - Teks kalimat dampak logout plural pada TC-FA-SU-109 dikutip dari TC-FA-SU-104.
  - Target TC (Gita Permata, Doni Prasetyo, Budi Santoso, Fajar Nugroho) adalah pengguna Pre-setup bersama; spec memakai pengguna milik spec dengan suffix (S-06).
