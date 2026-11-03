---
id: TC-FA-FAAM-E2E-247-pencatatan-absence-request-langsung-ditolak
title: "Pencatatan Absence: Request Langsung Tanpa Hak (Create, Edit, Delete, Bulk Delete) yang Ditolak Server Tidak Menulis Entri di Changelog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-611
  - TC-FA-FAAM-612
  - TC-FA-FAAM-613
  - TC-FA-FAAM-614
coverage:
  web: automated
---

# Pencatatan Absence: Request Langsung Tanpa Hak (Create, Edit, Delete, Bulk Delete) yang Ditolak Server Tidak Menulis Entri di Changelog

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor UI (pengamat Changelog): Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Sesi API aktor pengirim request langsung (login API password, token tidak dihitung sebagai sesi web; disediakan tim BE/FE): Read Only (No. 2; `Spectra.env.FA_RO_PASSWORD`), Create-Only (No. 4; `Spectra.env.FA_CO_PASSWORD`), dan Update-Only (No. 5; `Spectra.env.FA_UO_PASSWORD`). Klien HTTP untuk request langsung disediakan tim BE/FE; endpoint tidak disebut TC dan tidak dikarang spec. Payload request Create langsung valid selain bagian yang diuji.
- Env var: `FA_TC_PASSWORD`, `FA_RO_PASSWORD`, `FA_CO_PASSWORD`, `FA_UO_PASSWORD`.
- Data Dinamis, di-seed lewat API di hook `before`, nama bersuffix `{runId}-247`, Total Asset 0: `Edit Direct Item 612 {runId}-247` (Code `EDI612`; salinan fixture 13d), `Warehouse Pallet 613 {runId}-247` (Code `PLT-WH613`; salinan fixture 13), serta `Bulk Direct A 614 {runId}-247` dan `Bulk Direct B 614 {runId}-247` (salinan fixture 13c). Nama request Create: `Direct Create Item 611 {runId}-247` (tidak boleh tercipta setelah request ditolak).
- Kemampuan teknis: membuka Modal Changelog dan Search di dalamnya; membaca jumlah baris hasil Search sebelum aksi (baseline). Changelog adalah audit trail permanen sehingga hanya selisih terhadap baseline yang diasersi, bukan total absolut. Klien HTTP request langsung.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus seed milik spec ini lewat API dan hapus Asset Name apa pun yang ternyata terbentuk oleh request yang ditolak (seharusnya tidak ada).
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition: pengamat UI Total Control berada di Fixed Asset > Settings > Asset Master > Asset Name; sesi API berperan sebagaimana ditulis per langkah.

## Test Steps

### Baseline Changelog

1. Klik icon Changelog
2. Ketik Search `Edit Direct Item 612 {runId}-247`, tekan Enter
3. Catat jumlah baris Changelog sebagai baseline E
4. Ganti isi kotak search dengan `Warehouse Pallet 613 {runId}-247`, tekan Enter
5. Catat jumlah baris Changelog sebagai baseline W
6. Ganti isi kotak search dengan `Bulk Direct A 614 {runId}-247`, tekan Enter
7. Catat jumlah baris Changelog sebagai baseline BA
8. Ganti isi kotak search dengan `Bulk Direct B 614 {runId}-247`, tekan Enter
9. Catat jumlah baris Changelog sebagai baseline BB
10. Tutup Modal Changelog

### Request langsung yang ditolak (TC-FA-FAAM-611 sampai 614)

11. Kirim request langsung ke server: POST Create Asset Name `Direct Create Item 611 {runId}-247` memakai sesi API Read Only
12. Verifikasi server menolak dengan 403 Forbidden
13. Kirim request langsung ke server: PATCH Edit Asset Name `Edit Direct Item 612 {runId}-247` dengan Code `EDI612-X` memakai sesi API Create-Only
14. Verifikasi server menolak dengan 403 Forbidden
15. Kirim request langsung ke server: DELETE Asset Name `Warehouse Pallet 613 {runId}-247` memakai sesi API Update-Only
16. Verifikasi server menolak dengan 403 Forbidden
17. Kirim request langsung ke server: Bulk Delete `Bulk Direct A 614 {runId}-247` dan `Bulk Direct B 614 {runId}-247` memakai sesi API Update-Only
18. Verifikasi server menolak dengan 403 Forbidden

### Pengamatan Changelog

19. Muat ulang List dan klik icon Changelog
20. Ketik Search `Direct Create Item 611 {runId}-247`, tekan Enter
21. Verifikasi empty state `No results found` pada Changelog (TC-FA-FAAM-611: tanpa entri log)
22. Ganti isi kotak search dengan `Edit Direct Item 612 {runId}-247`, tekan Enter
23. Verifikasi jumlah baris Changelog sama dengan baseline E pada langkah 3 (TC-FA-FAAM-612: tanpa entri log baru)
24. Ganti isi kotak search dengan `Warehouse Pallet 613 {runId}-247`, tekan Enter
25. Verifikasi jumlah baris Changelog sama dengan baseline W pada langkah 5 (TC-FA-FAAM-613: tanpa entri log baru)
26. Ganti isi kotak search dengan `Bulk Direct A 614 {runId}-247`, tekan Enter
27. Verifikasi jumlah baris Changelog sama dengan baseline BA pada langkah 7 (TC-FA-FAAM-614: tanpa entri log baru untuk item A)
28. Ganti isi kotak search dengan `Bulk Direct B 614 {runId}-247`, tekan Enter
29. Verifikasi jumlah baris Changelog sama dengan baseline BB pada langkah 9 (TC-FA-FAAM-614: tanpa entri log baru untuk item B)
30. Tutup Modal Changelog

## Notes

- P-5(a): spec ini kelas g; pemicu kelas a (request langsung: TC-FA-FAAM-611 sampai 614) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji. Setiap TC memakai seed atau nama bersuffix dan baseline sendiri.
- Langkah 12, 14, 16, 18 (status 403) menjadi anchor positif bahwa pemicu benar-benar mencapai server sebelum asersi absence berikutnya; pembanding adalah jumlah awal yang dicatat pada langkah baseline.
- Langkah penghubung tanpa `Verifikasi`: seluruh langkah selain langkah berawalan `Verifikasi`, yaitu membuka dan mencari di Modal Changelog (S-12, S-14), mencatat baseline, mengirim pemicu, dan menutup modal secara deterministik.
- Urutan: seluruh nama dicatat pada Changelog sebelum request pertama, lalu seluruh pemicu, lalu pengamatan Changelog.
- Pembagian TC lintas spec: TC-FA-FAAM-611 sampai 614 juga ada di `sourceTc` spec 231 (butir status respons dan state data); id TC tetap di spec asalnya (satu TC satu spec asal) dan klausa log ada di spec ini. Butir status penolakan dan state data TC-FA-FAAM-842 ada pada TC-FA-FAAM-619 dan 620 (spec 233), TC-FA-FAAM-843 pada TC-FA-FAAM-621, 622, 623 (spec 250), TC-FA-FAAM-844 pada TC-FA-FAAM-631 (spec 248), dan TC-FA-FAAM-845 pada TC-FA-FAAM-105, 112, 120, 121 (spec 052).
- Pembagian TC absence lintas spec: TC-FA-FAAM-842 ada di spec 253, TC-FA-FAAM-843 di spec 254, TC-FA-FAAM-844 di spec 251, dan TC-FA-FAAM-845 di spec 252 (satu TC satu spec asal; dipisah dari spec ini agar tiap spec tidak melebihi batas langkah).
- Temuan untuk QA:
  - TC-FA-FAAM-611 sampai 614 tidak memuat langkah baca Changelog dengan nama yang dipakai request; spec memakai nama bersuffix unik dan baseline per seed.
