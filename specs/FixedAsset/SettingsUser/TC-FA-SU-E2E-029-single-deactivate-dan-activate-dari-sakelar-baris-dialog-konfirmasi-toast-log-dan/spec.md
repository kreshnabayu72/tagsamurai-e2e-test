---
id: TC-FA-SU-E2E-029-single-deactivate-dan-activate-dari-sakelar-baris-dialog-konfirmasi-toast-log-dan
title: "Single Deactivate dan Activate dari Sakelar Baris: Dialog, Konfirmasi, Toast, dan Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-87
  - TC-FA-SU-88
coverage:
  web: automated
---

# Single Deactivate dan Activate dari Sakelar Baris: Dialog, Konfirmasi, Toast, dan Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Lina Marlina`), password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip `seen`, sesi API aktor, pemulihan) mengikuti `suite.md`. Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise). Target aksi tulis tidak memakai pengguna Pre-setup bersama; spec memakai pengguna milik spec (S-06).
- Pengguna milik spec (dibuat lewat seed API di hook `before`, dihapus di hook `after`; nilai dirujuk lewat `Fixture.fa-settings-user.<kunci>`, fixture belum ada dan disediakan tim FE):
  - `Gita Permata {runId}-029`, email `gita.permata+{runId}-029@qwertysystem.net`: Active, tanpa aset aktif, bukan approver tertunggu (TC-FA-SU-87).
  - `Doni Prasetyo {runId}-029`, email `doni.prasetyo+{runId}-029@qwertysystem.net`: Inactive (TC-FA-SU-88).
- Kemampuan baca log (disediakan tim FE/BE, tanpa endpoint karangan): hook `before` mencatat baseline jumlah entri kedua pengguna pada Tab Changelog target, Tab System Log aktor, dan Activity Log. Log Activate dan Deactivate muncul eventual (NC-03): langkah yang menunggu entri memuat ulang tiap 5 detik, batas 2 menit. Entri dicari lewat Name bersuffix unik sehingga satu entri baru dibuktikan oleh selisih terhadap baseline.
- Tidak ada intercept, jam server, atau klien HTTP. State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-87: Deactivate satu pengguna dari sakelar baris

1. Ketik Search `Gita Permata {runId}-029`, tekan Enter
2. Klik sakelar Active pada baris `Gita Permata {runId}-029`
3. Verifikasi dialog Title `Deactivate User` dengan tombol close `[×]`, Body bullet `• Gita Permata {runId}-029`, kalimat `This user will be immediately logged out and blocked from entering FAMS.`, dan pertanyaan penutup `Are you sure you want to deactivate it?` tampil
4. Verifikasi tombol dialog `[Cancel]` (Text, Contrast) dan `[Deactivate]` (filled, severity danger)
5. Verifikasi dialog tanpa baris peringatan aset atau approval
6. Klik `[Deactivate]`
7. Verifikasi sakelar Active baris `Gita Permata {runId}-029` berpindah ke OFF
8. Verifikasi toast "Success, user has been deactivated." tampil
9. Verifikasi toast tampil di kanan bawah
10. Verifikasi dialog tertutup
11. Buka Detail `Gita Permata {runId}-029` > Tab Changelog, muat ulang sampai entri tampil
12. Verifikasi header Detail menampilkan status aktif Inactive dan badge status Inactive
13. Verifikasi Tab Changelog memuat tepat satu entri baru dengan Action `Deactivate`, Object `User`, Field `Status`, Old Value `Active`, New Value `Inactive`, dan Modified By `Lina M`
14. Buka Tab System Log aktor, cari Name `Gita Permata {runId}-029`
15. Verifikasi Tab System Log aktor memuat tepat satu entri baru ber-Name `Gita Permata {runId}-029` dengan Action `Deactivate`, Object `User`, Field `Status`, Old Value `Active`, New Value `Inactive`, dan Modified By `Lina M`
16. Buka Activity Log, cari Name `Gita Permata {runId}-029`
17. Verifikasi Activity Log memuat tepat satu entri baru ber-Name `Gita Permata {runId}-029` dengan Action `Deactivate`, Object `Settings > User`, dan Modified By `Lina M`
18. Kembali ke halaman User List

### TC-FA-SU-88: Activate satu pengguna dari sakelar baris

19. Ganti isi kotak search dengan `Doni Prasetyo {runId}-029`, tekan Enter
20. Klik sakelar Active pada baris `Doni Prasetyo {runId}-029`
21. Verifikasi dialog Title `Activate User`, Body bullet `• Doni Prasetyo {runId}-029`, kalimat `This user will regain access to the portal.`, dan pertanyaan `Are you sure you want to activate it?` tampil
22. Verifikasi tombol dialog `[Cancel]` (Text, Contrast) dan `[Activate]` (filled, severity primary)
23. Klik `[Activate]`
24. Verifikasi sakelar Active baris `Doni Prasetyo {runId}-029` berpindah ke ON
25. Verifikasi toast "Success, user has been activated." tampil
26. Buka Detail `Doni Prasetyo {runId}-029` > Tab Changelog, muat ulang sampai entri tampil
27. Verifikasi header Detail menampilkan status aktif Active
28. Verifikasi Tab Changelog memuat tepat satu entri baru dengan Action `Activate`, Object `User`, Field `Status`, Old Value `Inactive`, New Value `Active`, dan Modified By `Lina M`
29. Buka Tab System Log aktor, cari Name `Doni Prasetyo {runId}-029`
30. Verifikasi Tab System Log aktor memuat tepat satu entri baru ber-Name `Doni Prasetyo {runId}-029` dengan Action `Activate`, Object `User`, Field `Status`, Old Value `Inactive`, New Value `Active`, dan Modified By `Lina M`
31. Buka Activity Log, cari Name `Doni Prasetyo {runId}-029`
32. Verifikasi Activity Log memuat tepat satu entri baru ber-Name `Doni Prasetyo {runId}-029` dengan Action `Activate`, Object `Settings > User`, dan Modified By `Lina M`

## Notes

- Langkah penghubung (S-03): langkah 1 dan 19 (Search untuk menemukan baris target, R-16), langkah 14, 16, 29, dan 31 (mencari Name di surface log), dan langkah 18 (kembali ke User List).
- Pembagian TC lintas spec: TC-FA-SU-89 dan TC-FA-SU-90 (batal lewat `[Cancel]` dan `[×]`) ada di spec 039.
- Asersi "satu entri baru" memakai baseline hook `before` dan Name bersuffix unik (S-12); tidak ada total absolut audit trail yang diasersi.
- Temuan untuk QA:
  - TC-FA-SU-87 dan TC-FA-SU-88 Expected butir d menyebut tiga surface log tetapi tidak menyebut jalur navigasi Tab System Log aktor maupun Activity Log, dan tidak membedakan kolom yang tampil di tiap surface. Spec menulis kolom Action, Object, Field, Old Value, New Value, dan Modified By untuk Tab Changelog dan Tab System Log, dan hanya Action, Object `Settings > User`, Name, serta Modified By untuk Activity Log. Jalur navigasi ditentukan di Page Object.
  - Post Condition TC-FA-SU-87 butir b (penugasan Global Role, Group Role, Transaction Role, Home Group tetap tersimpan) dan butir d (Auth: sesi FAMS diakhiri, picker transaksi), serta TC-FA-SU-88 butir c (Auth), tidak punya langkah observasi di TC sehingga tidak diasersi.
  - Post Condition status aktif pada TC-FA-SU-87 dan TC-FA-SU-88 diasersi di header Detail karena langkah 4 TC membuka Detail.
  - Target TC (Gita Permata, Doni Prasetyo) adalah pengguna Pre-setup bersama; spec memakai pengguna milik spec bernama sama dengan suffix supaya Pre-setup tidak diubah (S-06). Pre-setup #21 disebut sebagai precondition TC-FA-SU-87 tetapi tidak dipakai langkah, sehingga tidak ditulis di Prerequisites.
  - Teks kalimat dampak logout dan teks toast yang disebut TC-FA-SU-87 dan TC-FA-SU-88 dikutip persis dari kedua TC itu.
