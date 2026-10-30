---
id: TC-GS-TAG-E2E-072-retensi-state-per-tab-dan-refresh
title: "Retensi State: Search/Filter Independen per Tab dan Dipulihkan Setelah Refresh"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-218
  - TC-GS-TAG-219
coverage:
  web: automated
---

# Retensi State: Search/Filter Independen per Tab dan Dipulihkan Setelah Refresh

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sari Dewi (Pre-setup TC, Client A) `totalControl_automated_qaTeam1@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Seed Registri A Client A (DD-01 sampai DD-30; 30 baris, 4 Paired dan 26 Not Paired; Tabel Data Uji Dinamis TC). Di-seed dan direset idempotent lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme tidak didefinisikan di TC, Q-4). Identifier TAG bersifat tetap dan tanpa sufiks `{runId}` (`suite.md`, S-12). Spec hanya membaca data; hitungan baris (26 baris Not Paired, 16 baris `generic` Official) valid hanya bila Seed Registri A utuh dan suite berjalan serial.
- General Settings: Date Format `dd/MM/yy`, 24-hour, Asia/Jakarta (default Client A); spec ini tidak mengubahnya.
- Suite serial (`parallel: false`).
- Flag Guided Tooltip registri (`guided_tooltip_seen_gs-tag-registry`) disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): state Search, Filter, Sort, dan halaman ketiga tab dikosongkan, termasuk penyimpanan sesi state tab yang dipakai langkah 31.
- Kemampuan teknis: memuat ulang halaman (F5) pada konteks browser yang sama supaya penyimpanan sesi tetap ada; membaca URL halaman (query parameter); membaca indikator sort, titik indikator Filter, dan teks pagination (selektor disediakan tim FE).

## Test Steps

### TC-GS-TAG-218: Search dan Filter independen per tab

1. Ketik Search `zebra`, tekan Enter
2. Klik ikon Filter untuk membuka panel
3. Pilih `Source` = Official
4. Klik `Apply`
5. Klik ikon Filter untuk menutup panel
6. Klik Tab Not Paired
7. Verifikasi tabel Tab Not Paired menampilkan data (pagination `Showing 1 - 10 of 26 TAGs`)
8. Verifikasi kotak Search Tab Not Paired kosong (tanpa keyword dari Tab All)
9. Verifikasi tidak ada filter aktif pada Tab Not Paired (tanpa titik indikator pada ikon Filter)
10. Ketik Search `alien`, tekan Enter
11. Klik Tab All
12. Verifikasi keyword `zebra` dipulihkan pada kotak Search Tab All
13. Verifikasi filter `Source` = Official dipulihkan pada Tab All
14. Verifikasi tab aktif tidak muncul sebagai query parameter URL
15. Klik `(←)` pada kotak Search
16. Klik ikon Filter untuk membuka panel
17. Klik `Clear Field`, lalu klik `Apply`
18. Klik ikon Filter untuk menutup panel
19. Klik Tab Not Paired
20. Klik `(←)` pada kotak Search

### TC-GS-TAG-219: Refresh halaman mempertahankan Search, Sort, Filter, dan pagination

21. Ketik Search `generic`, tekan Enter
22. Klik ikon Filter untuk membuka panel
23. Pilih `Source` = Official
24. Klik `Apply`
25. Klik ikon Filter untuk menutup panel
26. Klik header `Code` dua kali (descending)
27. Pindah ke halaman 2
28. Klik Tab All
29. Klik Tab Not Paired
30. Catat state Tab Not Paired (keyword `generic`, filter Official, sort `Code` descending, halaman 2)
31. Tekan F5
32. Verifikasi Tab Not Paired tetap aktif
33. Verifikasi tab aktif tidak muncul sebagai query parameter URL
34. Verifikasi keyword `generic` dipulihkan pada kotak Search Tab Not Paired
35. Verifikasi filter `Source` = Official dipulihkan pada Tab Not Paired
36. Verifikasi sort `Code` descending dipulihkan pada Tab Not Paired
37. Verifikasi halaman 2 dipulihkan pada Tab Not Paired
38. Klik Tab All
39. Verifikasi state Tab All tetap bersih (kotak Search kosong dan tanpa filter aktif)
40. Klik Tab Not Paired
41. Klik `(←)` pada kotak Search
42. Klik ikon Filter untuk membuka panel
43. Klik `Clear Field`, lalu klik `Apply`
44. Klik ikon Filter untuk menutup panel
45. Klik header `Code` sekali (kembali netral)

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber dipertahankan (218, 219). Spec tidak menghapus data. NC-04 (tab aktif dan state tab dipulihkan lewat penyimpanan sesi, bukan query parameter URL) menjadi dasar langkah 14, 32, dan 33; spec hanya mengasersi perilakunya.
- Panjang spec: 45 langkah, di atas sekitar 35 langkah. Alasan dipertahankan: kedua TC satu topik (retensi state tabel) pada satu dataset dan satu layar, dan langkah 15 sampai 20 mengosongkan state TC-GS-TAG-218 sehingga TC-GS-TAG-219 tidak bergantung pada hasilnya (S-09). Sekitar 14 langkah adalah pengosongan state (langkah 15 sampai 20 dan 40 sampai 45).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5, 18, 25, 44 (menutup panel), langkah 15 sampai 20 (mengosongkan state TC-GS-TAG-218 dan pindah ke Tab Not Paired untuk TC berikutnya), langkah 28 dan 29 (pindah tab, bagian langkah TC-GS-TAG-219), langkah 40 sampai 45 (mengosongkan state Tab Not Paired).
- Asersi tambahan di luar Expected TC (S-03): langkah 7 (anchor positif bahwa Tab Not Paired termuat sebelum absence keyword dan filter pada langkah 8 dan 9, bagian 8b butir 2).
- Pemisahan dari spec topik registri lain (Search, Filter, Sort, Pagination, Setup Column): kelas harness tidak sama dan tidak semua memakai data yang sama; ukuran gabungan semua topik registri melewati batas langkah jauh (KEPUTUSAN 2026-10-21, bagian 3 prinsip 1).
- Temuan untuk QA:
  - TC-GS-TAG-218 langkah 4 (mencari `alien` di Tab Not Paired) dan TC-GS-TAG-219 langkah 3 ("catat state") tidak punya Expected; spec tidak menambah asersi untuk keduanya.
  - TC-GS-TAG-219 butir c ("State Tab All tidak terpengaruh dan tetap bersih") tidak mendefinisikan "bersih" selain tanpa Search dan Filter; spec mengasersi kotak Search kosong dan tanpa filter aktif.
  - TC-GS-TAG-219 butir a menyebut "penyimpanan sesi" sebagai mekanisme pemulihan tab (NC-04), tetapi tidak menyatakan apakah state juga dipulihkan bila sesi login diganti; spec tidak menguji itu.
  - Hitungan baris bergantung pada Seed Registri A utuh dan suite serial (Q-4).
