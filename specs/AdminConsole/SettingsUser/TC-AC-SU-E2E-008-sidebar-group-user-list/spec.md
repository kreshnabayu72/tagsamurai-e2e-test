---
id: TC-AC-SU-E2E-008-sidebar-group-user-list
title: "Sidebar Group di User List: Screening, Filter Node beserta Descendant, Klik Ulang, dan Collapse"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-25
  - TC-AC-SU-26
  - TC-AC-SU-27
  - TC-AC-SU-28
coverage:
  web: automated
---

# Sidebar Group di User List: Screening, Filter Node beserta Descendant, Klik Ulang, dan Collapse

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-25 s.d. 28 | `Region A` | `Region A {runId}-008` | - | Group akar |
| TC-AC-SU-25 s.d. 28 | `Branch 1` | `Branch 1 {runId}-008` | - | anak `Region A {runId}-008` |
| TC-AC-SU-25 s.d. 28 | `Floor 1` | `Floor 1 {runId}-008` | - | anak `Branch 1 {runId}-008` |
| TC-AC-SU-25 s.d. 28 | `Branch 3` | `Branch 3 {runId}-008` | - | anak `Region A {runId}-008` |
| TC-AC-SU-25 s.d. 28 | `Region B` | `Region B {runId}-008` | - | Group akar |
| TC-AC-SU-26 | `Jane Smith` | `Jane Smith {runId}-008` | `janesmith+{runId}-008@qwertysystem.net` | Group Role aktif di `Floor 1 {runId}-008` |
| TC-AC-SU-26 | `Mike Tan` | `Mike Tan {runId}-008` | `miketan+{runId}-008@qwertysystem.net` | Group Role aktif di `Branch 3 {runId}-008` |
| TC-AC-SU-26 | `Rudi Hartono` | `Rudi Hartono {runId}-008` | `rudihartono+{runId}-008@qwertysystem.net` | hanya Global Role |
| TC-AC-SU-26 | `Sarah Lee` | `Sarah Lee {runId}-008` | `sarahlee+{runId}-008@qwertysystem.net` | Group Role tanpa group assignment |
| TC-AC-SU-26 | `Dedi Kurnia` | `Dedi Kurnia {runId}-008` | `dedikurnia+{runId}-008@qwertysystem.net` | Group Manager `Region A {runId}-008` |
| TC-AC-SU-26 | `Dewi Lestari` | `Dewi Lestari {runId}-008` | `dewilestari+{runId}-008@qwertysystem.net` | Total Control |
| TC-AC-SU-26 | `Rina Putri` | `Rina Putri {runId}-008` | `rinaputri+{runId}-008@qwertysystem.net` | Total Control |
| TC-AC-SU-26 | `Andi Wijaya` | `Andi Wijaya {runId}-008` | `andiwijaya+{runId}-008@qwertysystem.net` | Read Only |
| TC-AC-SU-26 | `John Doe` | `John Doe {runId}-008` | `johndoe+{runId}-008@qwertysystem.net` | Group Role aktif di `Region B {runId}-008` |

- Default User entitas (Total Control permanen, Pre-setup #1) tidak diubah. State collapse Sidebar Group disimpan di sisi klien (TC-AC-SU-28) dan dipulihkan ke expanded oleh langkah akhir blok.
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-25: Screening Sidebar Group

1. Amati Sidebar Group di kanan
2. Verifikasi Sidebar Group berada di sisi kanan
3. Verifikasi sidebar punya toggle collapse
4. Verifikasi header sidebar menampilkan judul `Groups`
5. Verifikasi header sidebar menampilkan tree search
6. Verifikasi header sidebar menampilkan tombol Expand/Collapse All
7. Verifikasi tidak ada tombol aksi Group maupun menu `⋯` per node
8. Klik tombol Expand All pada header sidebar
9. Verifikasi tree menampilkan node `Region A {runId}-008`, `Branch 1 {runId}-008`, `Floor 1 {runId}-008`, `Branch 3 {runId}-008`, dan `Region B {runId}-008` dengan arrow collapse/expand per node
10. Verifikasi tidak ada node greyed out atau hidden
11. Verifikasi tidak ada node terpilih
12. Ketik Search `{runId}-008`, tekan Enter
13. Verifikasi tabel menampilkan semua user seed (tidak tersaring node)

### TC-AC-SU-26: Klik node Sidebar Group memfilter user group dan seluruh descendant

14. Klik node `Region A {runId}-008`
15. Verifikasi node `Region A {runId}-008` tampil terpilih (highlighted)
16. Verifikasi tabel menampilkan `Jane Smith {runId}-008`, `Mike Tan {runId}-008`, `Dedi Kurnia {runId}-008`, `Dewi Lestari {runId}-008`, `Rina Putri {runId}-008`, dan `Andi Wijaya {runId}-008`
17. Verifikasi tabel tidak menampilkan `Rudi Hartono {runId}-008`, `Sarah Lee {runId}-008`, dan `John Doe {runId}-008`
18. Ganti isi kotak search dengan `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
19. Verifikasi tabel menampilkan Default User (Total Control permanen)
20. Ganti isi kotak search dengan `{runId}-008`, tekan Enter
21. Klik node `Region A {runId}-008` untuk membatalkan pilihan

### TC-AC-SU-27: Klik ulang node Sidebar aktif mengembalikan seluruh user

22. Klik node `Region A {runId}-008`
23. Klik node `Region A {runId}-008` lagi
24. Verifikasi node `Region A {runId}-008` tidak lagi terpilih
25. Verifikasi tabel menampilkan seluruh user seed entitas

### TC-AC-SU-28: Collapse Sidebar Group persisten setelah refresh

26. Klik toggle collapse Sidebar Group
27. Verifikasi sidebar ter-collapse
28. Tekan F5
29. Verifikasi sidebar tetap ter-collapse
30. Klik toggle collapse Sidebar Group untuk membuka kembali sidebar
31. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 8 (Expand All agar seluruh node terlihat; kondisi awal tree tidak disebut TC), langkah 12 (Search atas suffix spec, R-16), langkah 18 (Search untuk menemukan baris Default User, R-16), langkah 20 (kembali ke Search suffix), langkah 21 (batalkan pilihan node sebelum TC-AC-SU-27, S-09), langkah 30 (pulihkan sidebar expanded, S-09), langkah 31 (reset Search; sesudah F5 Search sudah kosong sehingga langkah ini menutup input). Layar awal dibuka hook `beforeEach` suite.
- Temuan untuk QA:
  - TC-AC-SU-25 butir b "seluruh node entitas" diasersi atas node seed milik spec; node group Pre-setup lain dan urutan seluruh tree tidak diasersi karena group Pre-setup tidak diubah dan jumlahnya tidak tetap.
  - TC-AC-SU-26 mengharapkan Default User tampil sebagai "TC permanen"; spec mengasersinya lewat Search atas email Pre-setup #1 pada node terpilih yang sama.
  - TC-AC-SU-28 "persisten setelah refresh" tidak menyebut tempat penyimpanan; spec hanya mengasersi perilaku UI.
  - Nama user TC (`Region A`, `Branch 1`, `Floor 1`, `Branch 3`, `Region B`, dan nama user TC) dipakai sebagai nama bersuffix `{runId}-008` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
