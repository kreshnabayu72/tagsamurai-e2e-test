---
id: TC-FA-SU-E2E-030-deactivate-dari-header-detail-dan-peringatan-aset-aktif-serta-approval-tertunda
title: "Deactivate dari Header Detail dan Dialog Peringatan Aset Aktif, Approval Tertunda, Kedua Peringatan, dan Tanpa Peringatan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-91
  - TC-FA-SU-92
  - TC-FA-SU-93
  - TC-FA-SU-94
  - TC-FA-SU-96
coverage:
  web: automated
---

# Deactivate dari Header Detail dan Dialog Peringatan Aset Aktif, Approval Tertunda, Kedua Peringatan, dan Tanpa Peringatan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Lina Marlina`), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip `seen`, sesi API aktor, pemulihan) mengikuti `suite.md`. Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Client `FaUserMain` (#20), Responsibilities #24 (pemegang aset aktif) dan #25 (approver tertunggu) sebagai pola data. Target aksi tulis memakai pengguna milik spec (S-06).
- Pengguna milik spec (seed API di hook `before`, dihapus di hook `after`; dirujuk lewat `Fixture.fa-settings-user.<kunci>`, fixture belum ada dan disediakan tim FE):
  - `Gita Permata {runId}-030`, email `gita.permata+{runId}-030@qwertysystem.net`: Active, tanpa aset aktif, bukan approver tertunggu (TC-FA-SU-96 dan TC-FA-SU-91).
  - `Budi Santoso Approver {runId}-030`, email `budi.approver+{runId}-030@qwertysystem.net`: Active, memegang aset aktif dan ditunggu sebagai approver (TC-FA-SU-94, hanya dibaca).
  - `Eka Wulandari {runId}-030`, email `eka.wulandari+{runId}-030@qwertysystem.net`: Active, approver permohonan Waiting for Approval, tanpa aset aktif (TC-FA-SU-93).
  - `Budi Santoso {runId}-030`, email `budi.santoso+{runId}-030@qwertysystem.net`: Active, memegang aset aktif `Laptop - 1 {runId}-030` dan `AC Split Ruang Kerja {runId}-030` (sedikitnya satu pada Borrowed Assets dan satu pada Assigned Assets), bukan approver tertunggu (TC-FA-SU-92).
- Kemampuan teknis: seed pemegang aset aktif dan approver tertunggu untuk pengguna milik spec (data modul Borrow, Assignment, Approvals) disediakan tim FE/BE; mekanisme tidak tertulis di TC (lihat Temuan untuk QA).
- Tidak ada intercept, jam server, atau klien HTTP. State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-96: Dialog Deactivate tanpa aset aktif dan tanpa approval tertunda

1. Ketik Search `Gita Permata {runId}-030`, tekan Enter
2. Klik sakelar Active pada baris `Gita Permata {runId}-030`
3. Verifikasi dialog hanya memuat bullet nama, kalimat dampak logout, dan pertanyaan penutup
4. Verifikasi tidak ada baris peringatan aset, approval, maupun kegagalan pemeriksaan
5. Klik `[Cancel]`

### TC-FA-SU-94: Dialog Deactivate dengan kedua peringatan

6. Ganti isi kotak search dengan `Budi Santoso Approver {runId}-030`, tekan Enter
7. Klik sakelar Active pada baris `Budi Santoso Approver {runId}-030`
8. Verifikasi urutan isi dialog: bullet nama, kalimat dampak logout `This user will be immediately logged out and blocked from entering FAMS.`, peringatan aset aktif `Budi Santoso Approver {runId}-030 is currently holding active assets (Borrowed / Assigned). Asset custody will remain recorded under this user until manually transferred or returned.`, peringatan approval tertunda `Budi Santoso Approver {runId}-030 is currently an approver for requests that are waiting for approval.`, lalu pertanyaan konfirmasi sebagai baris terakhir
9. Verifikasi kedua peringatan bersifat non-blocking dan tombol `[Deactivate]` Enabled
10. Klik `[Cancel]`

### TC-FA-SU-93: Dialog Deactivate dengan peringatan approval tertunda

11. Ganti isi kotak search dengan `Eka Wulandari {runId}-030`, tekan Enter
12. Klik sakelar Active pada baris `Eka Wulandari {runId}-030`
13. Verifikasi dialog memuat baris `Eka Wulandari {runId}-030 is currently an approver for requests that are waiting for approval.` tanpa angka jumlah permohonan
14. Verifikasi peringatan aset aktif tidak tampil
15. Verifikasi pertanyaan penutup `Are you sure you want to deactivate it?` tetap menjadi baris terakhir
16. Verifikasi tombol `[Deactivate]` Enabled
17. Klik `[Deactivate]`
18. Verifikasi sakelar Active baris `Eka Wulandari {runId}-030` berpindah ke OFF

### TC-FA-SU-92: Dialog Deactivate dengan peringatan aset aktif

19. Ganti isi kotak search dengan `Budi Santoso {runId}-030`, tekan Enter
20. Klik sakelar Active pada baris `Budi Santoso {runId}-030`
21. Verifikasi dialog Title `Deactivate User` memuat bullet `• Budi Santoso {runId}-030` dan kalimat dampak logout `This user will be immediately logged out and blocked from entering FAMS.`
22. Verifikasi baris peringatan `Budi Santoso {runId}-030 is currently holding active assets (Borrowed / Assigned). Asset custody will remain recorded under this user until manually transferred or returned.` tampil tanpa angka jumlah aset
23. Verifikasi pertanyaan `Are you sure you want to deactivate it?` selalu menjadi baris terakhir dialog
24. Verifikasi tombol `[Deactivate]` Enabled (tidak memblokir)
25. Klik `[Deactivate]`
26. Tunggu aksi selesai (sakelar Active baris `Budi Santoso {runId}-030` berstatus OFF)
27. Buka Detail `Budi Santoso {runId}-030` > Tab Responsibilities
28. Verifikasi header Detail menampilkan status aktif Inactive
29. Klik sub-tab Borrowed Assets
30. Verifikasi aset yang dipegang `Budi Santoso {runId}-030` tetap tercantum pada sub-tab Borrowed Assets
31. Klik sub-tab Assigned Assets
32. Verifikasi aset yang dipegang `Budi Santoso {runId}-030` tetap tercantum pada sub-tab Assigned Assets
33. Kembali ke halaman User List

### TC-FA-SU-91: Deactivate dan Activate dari sakelar header Detail

34. Ganti isi kotak search dengan `Gita Permata {runId}-030`, tekan Enter
35. Buka Detail `Gita Permata {runId}-030`
36. Klik sakelar Active di header Detail
37. Verifikasi dialog `Deactivate User` memuat copy identik dengan dialog baris: bullet `• Gita Permata {runId}-030`, kalimat dampak logout, dan pertanyaan `Are you sure you want to deactivate it?`
38. Klik `[Deactivate]`
39. Verifikasi sakelar Active di header berpindah ke OFF
40. Verifikasi label header berubah menjadi `Inactive`
41. Verifikasi badge status `Inactive` (danger) tampil
42. Verifikasi toast "Success, user has been deactivated." tampil
43. Klik sakelar Active di header Detail
44. Klik `[Activate]`
45. Verifikasi label header berubah menjadi `Active`
46. Verifikasi badge status `Active` (success) tampil
47. Verifikasi toast "Success, user has been activated." tampil

## Notes

- Alasan di atas 35 langkah: semua blok satu topik (dialog Deactivate dari sakelar baris dan header Detail) dan satu kelas harness (fungsional); tiap blok memakai pengguna milik spec sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Urutan blok: dialog yang hanya dibaca lebih dulu (TC-FA-SU-96, TC-FA-SU-94), lalu aksi yang menonaktifkan pengguna.
- Langkah penghubung (S-03): langkah 1 dan 34 (Search untuk menemukan baris target, R-16), langkah 6, 11, dan 19 (mengganti isi kotak search yang masih berisi nama sebelumnya, bagian 8b butir 9), langkah 5 dan 10 (menutup dialog yang hanya dibaca), langkah 26 (menunggu aksi `[Deactivate]` selesai sebelum berpindah ke Detail, bagian 8b butir 8), dan langkah 33 (kembali ke User List).
- Pembagian TC lintas spec: TC-FA-SU-87 dan TC-FA-SU-88 ada di spec 029; TC-FA-SU-95 (pemeriksaan gagal) ada di spec 032.
- Temuan untuk QA:
  - Pre-setup #24 dan #25 sama-sama menyebut Budi Santoso (aset aktif dan Pending Approvals 5 baris), sedangkan TC-FA-SU-92 hanya menyatakan peringatan aset dan TC-FA-SU-93 menyatakan peringatan aset tidak tampil untuk Eka Wulandari. Spec memakai dua pengguna terpisah (aset saja, aset dan approver) agar dialog TC-FA-SU-92 tidak memuat peringatan approval.
  - TC-FA-SU-92 menyebut aset `Laptop - 1` dan `AC Split Ruang Kerja` tanpa menyebut mana yang Borrowed dan mana yang Assigned; spec mengasersi aset yang dipegang tercantum pada kedua sub-tab.
  - Kalimat dampak logout pada TC-FA-SU-92, TC-FA-SU-94, dan TC-FA-SU-91 tidak ditulis utuh di TC itu; teksnya dikutip persis dari TC-FA-SU-87. TC-FA-SU-94 tidak menulis teks kedua peringatan; teksnya dikutip dari TC-FA-SU-92 dan TC-FA-SU-93.
  - Post Condition TC-FA-SU-91 butir b (dua entri berurutan `Deactivate` lalu `Activate` pada tiga surface log) tidak punya langkah observasi di TC sehingga tidak diasersi. Post Condition TC-FA-SU-92 butir c, TC-FA-SU-93 butir b (Auth) serta butir a (penugasan Approver tetap tersimpan) juga tidak punya langkah observasi dan tidak diasersi. Post Condition status aktif TC-FA-SU-92 diasersi di header Detail karena langkah 4 TC membuka Detail.
  - Mekanisme seed pemegang aset aktif dan approver tertunggu tidak disebut TC, PRD, atau LLD; spec menulisnya sebagai kemampuan "disediakan tim FE/BE" tanpa endpoint (R-19).
  - Target TC (Gita Permata, Budi Santoso, Eka Wulandari) adalah pengguna Pre-setup bersama; spec memakai pengguna milik spec dengan suffix (S-06).
