---
id: TC-FA-FAAC-E2E-089-delete-race-dan-halaman-terakhir
title: "Delete: Cek Ulang Server Saat Kondisi Berubah dan Halaman Terakhir Setelah Delete"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-223
  - TC-FA-FAAC-224
  - TC-FA-FAAC-703
coverage:
  web: automated
---

# Delete: Cek Ulang Server Saat Kondisi Berubah dan Halaman Terakhir Setelah Delete

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed Asset Class (kode literal TC, disediakan tim FE/BE lewat fixture BE): `B-RACE` tanpa Asset Name dan belum pernah diposting; `B-RACE2` tanpa Asset Name dan belum pernah diposting; sebelas Asset Class `B-PGDEL01` sampai `B-PGDEL11` (Class Name `Delete Fixture 01` sampai `Delete Fixture 11`), semuanya belum pernah diposting dan tanpa Asset Name. Satu Asset Name tanpa Asset Class tersedia untuk di-assign ke `B-RACE`.
- Ukuran halaman tabel 10 (default); hasil Search `B-PGDEL` berisi N = 11 baris menurut seed.
- Pelaku kedua: sesi API aktor (kemampuan suite, lihat suite.md): meng-assign Asset Name ke `B-RACE` dan mengisi Last Posted Period Mar 2026 pada `B-RACE2` lewat fixture BE, bukan sesi UI kedua.
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: assignment Asset Name pada `B-RACE`, Last Posted Period `B-RACE2`, dan `B-PGDEL11` yang terhapus.
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode dan nama itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-223: Asset Class menjadi dipakai Asset Name setelah dialog Delete dibuka

1. Ketik Search `B-RACE`, tekan Enter
2. Klik ikon `⋯` pada baris `B-RACE`, lalu pilih `Delete`
3. Lewat sesi API aktor, assign satu Asset Name ke `B-RACE` hingga assignment tersimpan
4. Klik `Delete` pada dialog
5. Verifikasi tidak ada toast yang tampil
6. Verifikasi Dialog Blok D-06 `Cannot Delete Asset Class` dengan `This asset class is used by 1 asset name.` tampil (cek ulang server menolak)
7. Klik `Cancel`
8. Verifikasi baris `B-RACE` masih ada di tabel (Asset Class tidak terhapus)

### TC-FA-FAAC-224: Asset Class diposting setelah dialog Delete dibuka

9. Ganti isi kotak search dengan `B-RACE2`, tekan Enter
10. Klik ikon `⋯` pada baris `B-RACE2`, lalu pilih `Delete`
11. Lewat sesi API aktor, isi Last Posted Period Mar 2026 untuk `B-RACE2` hingga nilainya tersimpan
12. Klik `Delete` pada dialog
13. Verifikasi tidak ada toast yang tampil
14. Verifikasi Dialog Blok D-05 `Cannot Delete Asset Class` dengan `This asset class was used in depreciation for Mar 2026.` tampil (cek ulang menolak)
15. Klik `Cancel`
16. Verifikasi baris `B-RACE2` masih ada di tabel (Asset Class tidak terhapus)

### TC-FA-FAAC-703: Menghapus baris terakhir di halaman terakhir memindahkan tabel ke halaman terakhir yang masih ada

17. Ganti isi kotak search dengan `B-PGDEL`, tekan Enter
18. Klik halaman 2
19. Verifikasi hasil Search `B-PGDEL` berisi 11 baris dan halaman 2 hanya memuat `B-PGDEL11`
20. Klik ikon `⋯` pada baris `B-PGDEL11`, lalu pilih `Delete`
21. Verifikasi Dialog `Delete Asset Class` berisi `• B-PGDEL11 – Delete Fixture 11` dan `This action cannot be undone. Are you sure you want to delete it?`
22. Klik `Delete`
23. Verifikasi toast sukses `Success, asset class has been deleted.`
24. Verifikasi tabel tidak menampilkan halaman 2 yang kosong dan pindah ke halaman terakhir yang masih ada (halaman 1)
25. Verifikasi halaman 1 menampilkan 10 baris `B-PGDEL01` sampai `B-PGDEL10`
26. Klik `(←)` pada kotak Search

## Notes

1. Urutan dalam spec: dua TC cek ulang server (ditolak, tanpa perubahan data) lebih dulu, lalu TC-703 yang menghapus baris di akhir.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 9, dan 17 (Search untuk menemukan baris target, R-16), langkah 7 dan 15 (menutup dialog), dan langkah 26 (mengosongkan Search). Langkah 3 dan 11 adalah pemicu pelaku kedua lewat sesi API (bukan kelas c; tidak memakai P-2).
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal dan asersi bergantung pada kode dan jumlah baris (11 baris `B-PGDEL`); kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. Temuan untuk QA: TC-223 dan TC-224 mensyaratkan Asset Class tanpa Asset Name yang lolos kedua guard, tetapi tidak menyebut Asset Name mana yang di-assign (TC-223) dan bagaimana pelaku kedua mengisi Last Posted Period (TC-224); keduanya ditulis sebagai kemampuan sesi API yang disediakan tim FE/BE tanpa endpoint (S-13).
