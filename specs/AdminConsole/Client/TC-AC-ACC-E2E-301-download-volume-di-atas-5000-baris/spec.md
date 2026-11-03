---
id: TC-AC-ACC-E2E-301-download-volume-di-atas-5000-baris
title: "Download Client List di Atas 5.000 Baris: Loading Screen Sampai Berkas Siap, Langsung Terunduh Tanpa Toast dan Tanpa Notifikasi"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-935
coverage:
  web: automated
---

# Download Client List di Atas 5.000 Baris: Loading Screen Sampai Berkas Siap, Langsung Terunduh Tanpa Toast dan Tanpa Notifikasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Kemampuan teknis: mengamati berkas yang terunduh di browser (nama berkas) dan membaca isinya (CSV/XLSX) di sisi test runner; disediakan tim FE. Tidak butuh intercept atau jam server.
- Fixture sementara A3 C-W3LST-4: 5.001 Client Archived `PT Volume Uji 0001` sampai `PT Volume Uji 5001` (Client Code `VOL-0001` sampai `VOL-5001`, Direct, Group Regional Timur, FAMS Archive, tanpa user ber-App Access) dibuat lewat skrip seed di hook `before` dan dihapus lewat skrip seed di hook `after`. Volume ini kelas e (5.001 baris); Search dan Filter tidak aktif saat Download.
- Kemampuan teknis: skrip seed massal (disediakan tim FE/BE); pembacaan berkas CSV besar di runner; membaca jumlah notifikasi belum dibaca pada ikon notifikasi navbar.

## Test Steps

### Download di atas 5.000 baris (TC-AC-ACC-935)

1. Klik sub-tab Archived
2. Verifikasi angka badge sub-tab Archived lebih besar dari 5.000
3. Catat angka badge sub-tab Archived dan jumlah notifikasi belum dibaca pada ikon notifikasi navbar (baseline)
4. Klik ikon Download lalu klik `Download as CSV`
5. Verifikasi loading screen tampil selama berkas disiapkan
6. Tunggu sampai berkas siap
7. Verifikasi loading screen hilang
8. Verifikasi tidak ada toast sukses maupun toast informasional
9. Verifikasi berkas `Clients.csv` langsung terunduh
10. Buka berkas `Clients.csv` dan hitung baris data (di luar baris header)
11. Verifikasi jumlah baris data sama dengan angka badge sub-tab Archived yang dicatat
12. Lihat ikon notifikasi navbar
13. Verifikasi jumlah notifikasi belum dibaca sama dengan baseline

## Notes

- Absence toast diletakkan sesudah loading screen hilang dan sebelum `Verifikasi` berkas (bagian 8b butir 11); klik pilihan format menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh.
- Kelas e (volume data khusus). Post Condition TC (`Hapus seed C-W3LST-4`) dipenuhi hook `after`.
- Temuan untuk QA
  - TC-AC-ACC-935: Expected (c) `loading screen hilang dan berkas langsung terunduh` bergantung pada indikator loading yang tidak dijelaskan selektornya; perlu aria-label.
