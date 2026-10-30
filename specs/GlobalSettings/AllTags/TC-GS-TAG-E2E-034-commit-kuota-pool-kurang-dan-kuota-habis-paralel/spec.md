---
id: TC-GS-TAG-E2E-034-commit-kuota-pool-kurang-dan-kuota-habis-paralel
title: "Commit: Kuota Pool Kurang Saat Submit dan Kuota Habis oleh Sesi Paralel (Rollback Penuh, Dialog 1 Varian Commit)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-TAG-106
  - TC-GS-TAG-107
coverage:
  web: automated
---

# Commit: Kuota Pool Kurang Saat Submit dan Kuota Habis oleh Sesi Paralel (Rollback Penuh, Dialog 1 Varian Commit)

## Prerequisites

- Mode: FE+BE (backend nyata; fixture BE sebagai pemicu kuota).
- Akun aktor: Total Control Client Quota Fitri Handayani `totalControl_automated_qaQuota@qwertysystem.net`, `Spectra.env.GS_TC_QUOTA_PASSWORD`. Login di hook `before`. Nama env `GS_TC_QUOTA_PASSWORD` belum terdaftar di `spectra.config.ts` dan `.env.example` (didaftarkan pemilik repositori).
- Pelaku kedua (TC-GS-TAG-107) memakai sesi API aktor (kemampuan dinyatakan di `suite.md`): admin kedua Client Quota yang mengaktivasi tag GPS `356938035643104` (identifier khusus untuk sesi kedua, tidak ada di stok maupun registri Client Quota) hingga kuota GPS habis. Akun tidak ada di Pre-setup TC; disediakan tim FE (S-13).
- Data Pre-setup (dipulihkan lewat fixture BE sebelum spec dan antar blok, kelas data-kuota prinsip 12): Client Quota plan Growth, kuota GPS 3 terpakai 0 (NFC 0), opsi mandiri aktif, registri GPS kosong. Katalog memuat Device Name `Queclink GV300` (Brand `Queclink`). IMEI `356938035643101` (DD-N1), `356938035643102` (DD-N2), `356938035643103` (DD-N3) tidak ada di stok (Self-Purchased dengan Template). IMEI `356938035643001` (DD-S1) pada TC-GS-TAG-107: stok resmi Client Quota yang Available (precondition tidak tertulis di TC; disediakan tim FE, lihat Temuan untuk QA).
- Kemampuan teknis (disediakan tim FE/BE): fixture BE yang mengurangi sisa kuota GPS Client Quota (TC-GS-TAG-106 langkah 4: sisa menjadi 1) dan mengembalikannya; seed/reset registri dan stok Client Quota; sesi API admin kedua; label dan placeholder input entri manual GPS serta tombol `Add` menunggu desain (NC-11), selektor disediakan tim FE.
- State global yang diubah: kuota GPS Client Quota (terpakai) diubah fixture BE dan dipulihkan di hook `after` (tidak berasumsi seeding berhasil penuh), beserta registri Client Quota dan staging yang tersisa.
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Suite serial (`parallel: false`). Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-TAG-106: Kuota pool kurang saat Submit

1. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik [Continue] pada popup `Ready to Activate a TAG`
2. Isi Template Device Name `Queclink GV300`, Brand `Queclink`
3. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643101`, `356938035643102`, `356938035643103`
4. Lewat fixture backend, kurangi sisa kuota GPS Client Quota menjadi 1
5. Klik [Submit], lalu klik [Submit] pada dialog (konfirmasi)
6. Verifikasi dialog `Insufficient Quota` dengan body "Insufficient license quota to activate the submitted TAGs."
7. Verifikasi baris rincian "GPS: need 3, only 1 available."
8. Verifikasi tombol [OK] tampil pada dialog
9. Verifikasi tabel staging utuh (tiga baris tetap: `356938035643101`, `356938035643102`, `356938035643103`)
10. Klik [OK]
11. Klik item sidebar `TAG`, klik [Leave] pada dialog Unsaved Changes (membuang staging), lalu klik Tab All
12. Ketik Search `35693803564310`, tekan Enter
13. Verifikasi empty state "No results found" (nol baris ter-commit)

### TC-GS-TAG-107: Kuota habis oleh sesi paralel antara re-check dan penulisan

14. Pulihkan registri dan kuota Client Quota ke kondisi awal lewat fixture BE, lalu atur sisa kuota GPS menjadi 1
15. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik [Continue] pada popup `Ready to Activate a TAG`
16. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643001`
17. Dari sesi kedua (admin kedua Client Quota, sesi API), aktivasi tag GPS `356938035643104` hingga kuota GPS habis tersimpan
18. Klik [Submit], lalu klik [Submit] pada dialog (konfirmasi)
19. Verifikasi dialog `Insufficient Quota` varian commit tampil
20. Verifikasi staging tetap berisi baris `356938035643001`
21. Klik [OK]
22. Klik item sidebar `TAG`, klik [Leave] pada dialog Unsaved Changes (membuang staging), lalu klik Tab All
23. Ketik Search `356938035643001`, tekan Enter
24. Verifikasi empty state "No results found" (tidak ada baris ter-commit; rollback total, bukan partial)

## Notes

- Mode: FE+BE. Kelas data-kuota (prinsip 12, perluasan e). Fixture BE hanya pemicu state kuota, bukan objek asersi.
- Langkah penghubung (tanpa `Verifikasi`, S-03): 1, 10, 11, 14, 15, 21, 22 (membuka sesi, menutup dialog, membuang staging, pemulihan); langkah 12, 13, 23, 24 memakai empty state hasil Search sebagai anchor absence yang sah (8b butir 2) untuk "nol baris ter-commit".
- Langkah 24 menjadi anchor positif lewat pemicu langkah 17 (registri memuat tag lain dari sesi kedua) dan hasil Search yang diproses.
- Pembagian TC lintas spec: TC-GS-TAG-13 (kartu 60 of 50) bersama gate kuota Activate (Client Over) berada di spec lain.
- Temuan untuk QA:
  - Q-5: pemicu "antara re-check dan penulisan" (TC-GS-TAG-107) tidak deterministik; spec memakai sesi API admin kedua sebelum Submit, bukan tepat di tengah commit.
  - TC-GS-TAG-107: TC tidak menyebut apakah `356938035643001` adalah stok resmi Client Quota atau Self-Purchased dengan Template; tanpa Template baris menjadi Needs Info dan Submit diblokir T-05. Spec mengasumsikan stok resmi Available dan meminta tim FE menyediakannya. Akun admin kedua Client Quota tidak ada di Pre-setup. TC-GS-TAG-107 tidak menyebut identifier tag GPS yang diaktivasi sesi kedua; spec memakai `356938035643104` sebagai identifier khusus.
  - TC-GS-TAG-107 Expected a tidak menyebut body dan rincian dialog varian commit; rincian jumlah (need/only) tidak diasersi. Nama tombol dialog varian commit diasumsikan sama dengan TC-GS-TAG-106 ([OK]).
  - TC-GS-TAG-106 langkah 4: "kurangi sisa kuota GPS" lewat fixture BE tidak menyebut mekanismenya; disediakan tim FE/BE.
  - Post Condition kedua TC bernilai `-`.
