---
id: TC-GS-TAG-E2E-087-logging-activate-event-log-activity-log-dan-tanpa-entri-saat-batal
title: "Pencatatan Activate: Satu Event Log dan Satu Activity Log per Operasi, Per Outcome, dan Tanpa Entri saat Submit Kosong atau Dibatalkan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-263
  - TC-GS-TAG-264
  - TC-GS-TAG-269
coverage:
  web: automated
---

# Pencatatan Activate: Satu Event Log dan Satu Activity Log per Operasi, Per Outcome, dan Tanpa Entri saat Submit Kosong atau Dibatalkan

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Client A Sari Dewi (`Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup TC); kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before` (akun default suite), sehingga hook `after` tidak mengganti sesi.
- Flag Guided Tooltip `gs-tag-registry` dan `gs-tag-activate` mengikuti hook suite `before` dan `after` (lihat `suite.md`, bagian Hook Guided Tooltip).
- Suite serial (`parallel: false`). Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- Data (dipulihkan oleh hook `before` ke kondisi awal lewat fixture BE; mekanisme disediakan tim FE/BE, lihat Temuan untuk QA):
  - Stok resmi Client A: GPS `356938035643001` (DD-S1) dan `356938035643003` (DD-S3) Available (Device Name `Teltonika FMB920`, SKU `SKU-GPS-01`); Template Self-Purchased kosong.
  - DD-N1 `356938035643101` (GPS tidak ada di stok) dan DD-N4 `356938035643201` (GPS In Use di Client B, pemilik Total Control Client B Kartika Sari `totalControl_automated_qaTeam2@qwertysystem.net`; kepemilikan unit dibuat lewat fixture BE, tanpa login Client B). Dipakai hanya untuk membangun sesi TC-264 lewat fixture BE; kolisi menghasilkan Waiting for Approval.
  - Seed Registri A (DD-02 `E2801160600002054D8A0002` dipakai TC-269; dibatalkan, tidak berubah).
- Sesi API aktor (kemampuan dinyatakan di `suite.md`): admin kedua memicu sesi paralel TC-264 (langkah 19).
- Pemicu sesi TC-264 (langkah 19): sesi Activate GPS selesai dengan 001 dan 003 Activated, 201 Waiting for Approval, 101 Failed karena diaktivasi sesi lain pada saat yang sama. Pemicu sesi paralel dan "tepat saat commit" memakai fixture BE lewat sesi API admin kedua (Q-5), disediakan tim FE/BE, dan melalui jalur commit produk sehingga Event Log dan Activity Log tercatat.
- Baseline log: Event Log dan Activity Log menumpuk antar spec (tidak dibersihkan), sehingga semua asersi entri baru memakai selisih total terhadap baseline yang dicatat sebelum aksi (S-12); tiap blok mencatat baseline sendiri (`N0`/`A0`, `N1`/`A1`, `N2`/`M2`/`A2`). Total Event Log dibaca dari footer `Showing ... of N logs`; total Activity Log dibaca dari footer tab User Action dengan Filter Action `Activate TAG` (langkah 2, 12, 17, dan 27) atau tanpa filter (langkah 30 dan 43).
- Kemampuan teknis: entri manual GPS (input lalu klik `Add`; label dan placeholder menunggu desain, NC-11); mengganti sesi API admin kedua; pembaca nilai footer pagination.
- State global yang diubah: tidak ada selain data (stok, registri, dan log). Spec ini mereset dataset yang dipakainya di hook `before` sendiri; hook `after` suite memulihkan Seed Registri A dan stok resmi secara idempotent (pernyataan hook di `suite.md`).

## Test Steps

### TC-GS-TAG-263: Activate sukses mencatat satu Event Log dan satu Activity Log per operasi

1. Klik tombol `Event Log` di toolbar, catat total `N0` pada footer Tab Activate TAG (`Showing ... of N0 logs`), lalu tutup modal lewat `✕`
2. Buka Global Settings > Activity Log, tab User Action, filter Action `Activate TAG`, catat total entri `A0` pada footer
3. Buka Global Settings > TAG, Tab All
4. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik `Continue` pada popup `Ready to Activate a TAG`
5. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643001`
6. Tambahkan lewat entri manual `356938035643003`
7. Klik `Submit` lalu konfirmasi
8. Tunggu aksi selesai
9. Buka Event Log, Tab Activate TAG
10. Verifikasi total log menjadi `N0 + 1` (footer `of N0+1 logs`)
11. Verifikasi baris pertama (Date terbaru): TAG Type `GPS`, Activity `Activate`, Success `2`, Waiting for Approval `0`, Failed `0`, Hardware `—`, PIC `Sari D`
12. Tutup modal Event Log lewat `✕`, buka Global Settings > Activity Log, tab User Action, filter Action `Activate TAG`
13. Verifikasi total entri menjadi `A0 + 1`
14. Verifikasi entri teratas (Date terbaru): Object `TAG Registry`, Action `Activate TAG`, Name `GPS`, Field `Status`, Old Value `—`, New Value `Activated 2, Waiting for Approval 0, Failed 0`
15. Ketik Search `356938035643001`, tekan Enter
16. Verifikasi empty state `No results found` tampil (tidak ada entri per-tag di Activity Log)

### TC-GS-TAG-264: Activate dengan Waiting for Approval dan Failed dicatat per outcome

17. Kosongkan Search dengan klik `(←)` pada kotak Search, lalu catat total entri `A1` pada footer
18. Buka Global Settings > TAG, Tab All, klik tombol `Event Log`, catat total `N1` pada footer Tab Activate TAG, lalu tutup modal lewat `✕`
19. Pulihkan dataset lewat fixture BE (tag `356938035643001` dan `356938035643003` kembali Available dan keluar dari registri Client A), lalu bangun sesi Activate GPS selesai: `356938035643001` dan `356938035643003` (Official) Activated, `356938035643201` (kolisi) Waiting for Approval, `356938035643101` Failed karena diaktivasi sesi lain pada saat yang sama
20. Buka Global Settings > TAG, Tab All, klik tombol `Event Log`
21. Verifikasi total log menjadi `N1 + 1`
22. Verifikasi baris pertama (Date terbaru): Success `2`, Waiting for Approval `1`, Failed `1`
23. Klik `Detail` pada baris pertama
24. Verifikasi section `Activated` memuat 2 baris
25. Verifikasi section `Waiting for Approval` memuat 1 baris
26. Verifikasi section `Failed` tidak tampil (baris Failed tidak ada)
27. Tutup popup dan modal Event Log lewat `✕`, buka Global Settings > Activity Log, tab User Action, filter Action `Activate TAG`
28. Verifikasi total entri menjadi `A1 + 1`
29. Verifikasi entri teratas: Field `Status`, Old Value `—`, New Value `Activated 2, Waiting for Approval 1, Failed 1`

### TC-GS-TAG-269: Submit kosong dan aksi yang dibatalkan tidak menghasilkan entri log

30. Buka Global Settings > Activity Log, tab User Action, tanpa filter, catat total entri `A2` pada footer
31. Buka Global Settings > TAG, Tab All, klik tombol `Event Log`, catat total `N2` pada footer Tab Activate TAG, klik tab `Audit TAG`, catat total `M2` pada footer, lalu tutup modal lewat `✕`
32. Klik `+ Activate TAG`, pilih `GPS`, klik `Continue`
33. Klik `Submit` pada staging kosong
34. Tunggu aksi selesai, lalu buka Global Settings > TAG, Tab All
35. Klik `Audit TAG`, pilih `RFID` pada overlay `Select TAG Type`
36. Tutup popup Audit lewat `✕` tanpa Submit
37. Ketik Search `E2801160600002054D8A0002`, tekan Enter
38. Buka menu baris DD-02, klik `Delete`, lalu klik `Cancel` pada dialog
39. Buka Event Log, Tab Activate TAG
40. Verifikasi total log sama dengan `N2` (footer `of N2 logs`)
41. Klik tab `Audit TAG`
42. Verifikasi total log sama dengan `M2`
43. Tutup modal lewat `✕`, buka Global Settings > Activity Log, tab User Action, tanpa filter
44. Verifikasi total entri sama dengan `A2`

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular. Kelas g ringan (TC-269) ditulis di spec asal dengan baseline sesuai keputusan D-1; tidak ada spec absence terpisah untuk TC-269.
- P-1 (state berat): klausa absence TC-263 c (tidak ada entri per-tag di Activity Log, langkah 16) bergantung pada sesi Activate yang baru dibangun langkah 4 sampai 8; anchor positifnya entri GPS pada langkah 14 (bagian 8b butir 2). TC-269 adalah asersi berbaseline (S-12): total `N2`, `M2`, dan `A2` dicatat langkah 30 sampai 31 sebelum aksi pemicu, sehingga tidak memakai P-1.
- Urutan TC dalam spec sama dengan sumber (263, 264, 269). TC-264 membutuhkan stok `356938035643001` dan `356938035643003` kembali Available (langkah 19), karena TC-263 sudah mengaktivasinya.
- Alasan spec di atas sekitar 35 langkah (44 langkah): tiga TC memakai satu alur (Activate GPS) dan dua surface log yang sama; blok berurutan dan saling membutuhkan baseline `N0` dan `A0`, sehingga pemisahan menambah login dan pencatatan baseline. Tidak ada langkah berulang dengan ekspansi.
- Langkah penghubung (tanpa `Verifikasi`, tidak ada di TC): langkah 1, 2, 17, 18, 30, 31 (pencatatan baseline sebelum aksi pemicu, S-12), langkah 3, 12, 17, 20, 27, 34, 43 (pindah surface dan mengosongkan Search), langkah 8 (Tunggu aksi selesai, bagian 8b butir 8), langkah 19 (precondition TC-264 dibangun fixture BE; dipakai sebagai precondition, hasil diasersi pada langkah 21 sampai 29), langkah 37 (mencari DD-02 agar baris target tampil).
- Langkah 16 (empty state `No results found`) memakai entri GPS pada langkah 14 sebagai anchor positif.
- Temuan untuk QA:
  - TC-264 berlabel `Manual Only — (d) dua sesi paralel` dan tidak menyebut cara memicu Failed (aktivasi sesi lain pada saat yang sama); spec membangun sesi lewat fixture BE lewat jalur commit produk (Q-5) dan menulis pemicu sebagai kemampuan disediakan tim FE/BE tanpa endpoint karangan.
  - TC-264 langkah 2 ("Klik `Detail` pada baris terbaru") tidak membedakan baris TC-263 dan TC-264 bila dua sesi dicatat; spec mengidentifikasi baris terbaru lewat selisih total terhadap baseline.
  - TC-263 dan TC-264 memakai identifier tetap (`356938035643001`, `...003`) pada satu client sehingga run kedua spec ini memerlukan pemulihan fixture BE (Q-4).
  - TC-269 langkah 1 ("klik `Submit` pada staging kosong") tidak menyebut respons UI (Toast T-18 menurut spec 030); spec tidak mengasersinya karena Expected TC-269 hanya jumlah log.
  - TC-269 Expected "jumlah baris Event Log dan entri Activity Log tidak bertambah" tidak menyebut tab Event Log mana; spec membandingkan kedua tab Event Log dan total Activity Log tab User Action.
