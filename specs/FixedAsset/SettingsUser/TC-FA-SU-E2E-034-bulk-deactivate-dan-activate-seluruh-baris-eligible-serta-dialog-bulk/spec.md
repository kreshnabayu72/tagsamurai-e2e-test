---
id: TC-FA-SU-E2E-034-bulk-deactivate-dan-activate-seluruh-baris-eligible-serta-dialog-bulk
title: "Bulk Deactivate dan Activate Seluruh Baris Eligible serta Dialog Bulk"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-104
  - TC-FA-SU-105
  - TC-FA-SU-106
  - TC-FA-SU-108
coverage:
  web: automated
---

# Bulk Deactivate dan Activate Seluruh Baris Eligible serta Dialog Bulk

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Lina Marlina`), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip `seen`, sesi API aktor, pemulihan) mengikuti `suite.md`. Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Client `FaUserMain` (#20), Responsibilities #24 dan #25 sebagai pola data. Target aksi tulis memakai pengguna milik spec (S-06). TC-FA-SU-108 menyebut Pre-setup #36 (Client `FaUserSel`, 120 pengguna); spec memakai 12 pengguna Active milik spec di `FaUserMain` (lihat Temuan untuk QA).
- Pengguna milik spec (seed API di hook `before`, dihapus di hook `after`; dirujuk lewat `Fixture.fa-settings-user.<kunci>`, fixture belum ada dan disediakan tim FE). Email `<alias>+{runId}-034@qwertysystem.net` dengan alias huruf kecil:
  - TC-FA-SU-104: `U104A {runId}-034` dan `U104B {runId}-034`, keduanya Active.
  - TC-FA-SU-105: `U105A {runId}-034` dan `U105B {runId}-034`, keduanya Inactive.
  - TC-FA-SU-106: `Budi Santoso U106 {runId}-034` (Active, memegang aset aktif), `Eka Wulandari U106 {runId}-034` (Active, approver permohonan Waiting for Approval, tanpa aset aktif), dan `Gita Permata U106 {runId}-034` (Active, bersih).
  - TC-FA-SU-108: `U108-01 {runId}-034` sampai `U108-12 {runId}-034`, seluruhnya Active (12 baris, melebihi 10 baris satu halaman).
- Kemampuan teknis: seed pemegang aset aktif dan approver tertunggu untuk pengguna milik spec disediakan tim FE/BE; kemampuan baca log (disediakan tim FE/BE, tanpa endpoint karangan): hook `before` mencatat baseline jumlah entri tiap pengguna milik spec pada Tab Changelog target serta total entri Tab System Log aktor dan Activity Log. Log muncul eventual (NC-03): langkah yang menunggu entri memuat ulang tiap 5 detik, batas 2 menit.
- Seleksi bertahan lintas halaman (TC-FA-SU-120); tidak ada intercept, jam server, atau klien HTTP. State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-104: Bulk Deactivate seluruh baris eligible

1. Ketik Search `U104`, tekan Enter
2. Centang `U104A {runId}-034` dan `U104B {runId}-034`
3. Verifikasi Bulk Actions Bar muncul dengan counter `2 Users selected`
4. Klik Bulk Action > `[Deactivate]`
5. Verifikasi dialog Title `Deactivate Users` dengan bullet `• U104A {runId}-034` dan `• U104B {runId}-034`, kalimat `These users will be immediately logged out and blocked from entering FAMS.`, dan penutup `Are you sure you want to deactivate them?`
6. Klik `[Deactivate]` pada dialog
7. Verifikasi toast "Success, user has been deactivated." tampil
8. Verifikasi sakelar Active `U104A {runId}-034` dan `U104B {runId}-034` OFF
9. Verifikasi seleksi di-reset dan Bulk Actions Bar tidak tampil
10. Verifikasi satu entri `Deactivate` per pengguna (`U104A {runId}-034` dan `U104B {runId}-034`) pada Tab Changelog target, Tab System Log aktor, dan Activity Log

### TC-FA-SU-105: Bulk Activate seluruh baris eligible

11. Ganti isi kotak search dengan `U105`, tekan Enter
12. Centang `U105A {runId}-034` dan `U105B {runId}-034`
13. Klik Bulk Action > `[Activate]`
14. Verifikasi dialog Title `Activate Users` dengan bullet `• U105A {runId}-034` dan `• U105B {runId}-034`, kalimat `These users will regain access to the portal.`, dan penutup `Are you sure you want to activate them?`
15. Klik `[Activate]` pada dialog
16. Verifikasi toast "Success, user has been activated." tampil
17. Verifikasi sakelar Active `U105A {runId}-034` dan `U105B {runId}-034` ON
18. Verifikasi seleksi di-reset
19. Verifikasi satu entri `Activate` per pengguna (`U105A {runId}-034` dan `U105B {runId}-034`) pada Tab Changelog target, Tab System Log aktor, dan Activity Log

### TC-FA-SU-106: Dialog Bulk Deactivate dengan peringatan per kelompok

20. Ganti isi kotak search dengan `U106`, tekan Enter
21. Centang `Budi Santoso U106 {runId}-034`, `Eka Wulandari U106 {runId}-034`, dan `Gita Permata U106 {runId}-034`
22. Klik Bulk Action > `[Deactivate]`
23. Verifikasi setelah kalimat dampak muncul kelompok `The following users are currently holding active assets (Borrowed / Assigned). Asset custody will remain recorded under each user until manually transferred or returned:` dengan bullet `• Budi Santoso U106 {runId}-034`
24. Verifikasi kelompok `The following users are currently approvers for requests that are waiting for approval:` dengan bullet `• Eka Wulandari U106 {runId}-034`
25. Verifikasi pertanyaan `Are you sure you want to deactivate them?` menjadi baris terakhir
26. Klik `[Cancel]`

### TC-FA-SU-108: Dialog Bulk menampilkan seluruh nama tanpa diringkas

27. Klik `[Unselect All]`
28. Ganti isi kotak search dengan `U108`, tekan Enter
29. Centang 10 baris pada halaman 1, pindah ke halaman 2, lalu centang 2 baris sisanya (12 pengguna `U108-01` sampai `U108-12`)
30. Klik Bulk Action > `[Deactivate]`
31. Verifikasi seluruh 12 nama terpilih tampil sebagai bullet tanpa ringkasan jumlah
32. Gulir daftar nama pada body dialog
33. Verifikasi body dialog memiliki tinggi maksimum tetap dan daftar di dalamnya yang scroll
34. Verifikasi tombol `[Cancel]` dan `[Deactivate]` tetap terlihat
35. Klik `[Cancel]`
36. Klik `[Unselect All]`

## Notes

- Alasan sekitar 35 langkah (36): semua blok satu topik (aksi Bulk Deactivate dan Activate beserta dialognya) dan satu kelas harness (fungsional); tiap blok memakai pengguna milik spec sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16), langkah 11, 20, dan 28 (mengganti isi kotak search yang masih berisi nilai sebelumnya, bagian 8b butir 9), langkah 26, 35 (menutup dialog yang hanya dibaca), langkah 27 dan 36 (membersihkan seleksi, S-09), dan langkah 32 (menggulir daftar nama).
- Pembagian TC lintas spec: TC-FA-SU-109, TC-FA-SU-110, dan TC-FA-SU-111 (seleksi campuran) ada di spec 035.
- Temuan untuk QA:
  - TC-FA-SU-108 menyebut Pre-setup #36 (Client `FaUserSel`, 120 pengguna) padahal akun aktor #1 ada di tenant `FaUserMain` dan akun Total Control tenant `FaUserSel` tidak tertulis. Tujuan TC (lebih dari 10 baris) tidak bergantung pada 120 pengguna, sehingga spec memakai 12 pengguna Active milik spec di `FaUserMain`.
  - TC-FA-SU-106 Expected butir b menyebut "kelompok hanya tampil bila minimal satu baris terpilih memenuhi syarat" tanpa langkah yang menguji kebalikannya; klausa itu tidak diasersi.
  - Post Condition TC-FA-SU-104 butir c dan TC-FA-SU-105 butir c (Auth: sesi FAMS diakhiri, picker transaksi) tidak punya langkah observasi di TC dan tidak diasersi. Post Condition butir a dan b diasersi lewat Expected padanan (langkah 7 sampai 10 dan 16 sampai 19).
  - Kalimat dampak logout plural dan teks toast pada TC-FA-SU-104 dan TC-FA-SU-105 dikutip persis dari TC-FA-SU-104 dan TC-FA-SU-105. TC tidak menyebut jalur navigasi Tab System Log aktor dan Activity Log; asersi log memakai kemampuan baca log.
  - Target TC (Budi Santoso, Eka Wulandari, Gita Permata, dan nama generik) adalah pengguna Pre-setup bersama; spec memakai pengguna milik spec dengan suffix (S-06).
