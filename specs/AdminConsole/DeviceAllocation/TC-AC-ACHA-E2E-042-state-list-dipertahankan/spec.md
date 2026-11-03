---
id: TC-AC-ACHA-E2E-042-state-list-dipertahankan
title: "State List Device Allocation Dipertahankan atau Dibuang"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-366
  - TC-AC-ACHA-367
  - TC-AC-ACHA-369
coverage:
  web: automated
---

# State List Device Allocation Dipertahankan atau Dibuang

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #21) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (entitas PT ABC), password `Spectra.env.AC_TC_PASSWORD` (nama env tercantum di daftar env var `suite.md`, didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before`/`after` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor (lihat `suite.md`).
- Data Pre-setup: Seed 30 alokasi (Pre-setup #48, rincian Seed List) yang dilihat Total Control Principal sebagai seluruh 30 baris, Page size default 10 (tiga halaman). Nilai seed dirujuk lewat fixture `AdminConsoleDeviceAllocation`. Allocation ID, Allocated By, dan Last Updated seed bernilai literal dan diasersi (pengecualian S-12 nama literal, Lampiran A butir A-6: seeding idempotent, tidak diubah atau dihapus oleh spec ini, suite serial). Tidak ada Data Dinamis kecuali disebut di bawah.
- Kemampuan teknis (disediakan tim FE): Logout lalu Login ulang akun aktor di browser yang sama (TC-AC-ACHA-369). Muat ulang halaman (F5).
- State yang diubah: Search, Filter, Sort, Page size, dan halaman aktif dikembalikan ke default di akhir tiap TC; hook `after` mengembalikan sesi ke akun default suite.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-AC-ACHA-366: State List dipertahankan setelah F5

1. Ketik Search `Budi`, tekan Enter
2. Klik ikon Filter
3. Pilih Status `Completed`, klik `[Apply]`
4. Tutup Filter Panel (klik ikon Filter)
5. Klik header kolom Quantity sekali (ascending)
6. Ubah Page size menjadi `25`
7. Klik Allocation ID `HALC-20260901-00001`
8. Tutup modal Allocation Log lewat ikon close `[×]`
9. Verifikasi setelah menutup modal Allocation Log Search `Budi` tetap
10. Verifikasi setelah menutup modal Allocation Log Filter Status `Completed` tetap
11. Verifikasi setelah menutup modal Allocation Log Sort Quantity ascending tetap
12. Verifikasi setelah menutup modal Allocation Log Page size 25 tetap
13. Muat ulang halaman (F5)
14. Verifikasi setelah F5 kotak Search masih berisi `Budi`
15. Verifikasi setelah F5 badge titik pada ikon Filter masih tampil (Filter Status `Completed` dipertahankan)
16. Verifikasi setelah F5 indikator sort Quantity ascending (`↑`) dipertahankan
17. Verifikasi setelah F5 halaman aktif dipertahankan (halaman 1)
18. Verifikasi setelah F5 Page size 25 dipertahankan (bukan reset ke default)
19. Klik `(←)` pada kotak Search
20. Klik ikon Filter
21. Klik `[Clear Field]`, klik `[Apply]`
22. Tutup Filter Panel (klik ikon Filter)
23. Klik header kolom Quantity dua kali hingga netral
24. Ubah Page size menjadi `10`

### TC-AC-ACHA-367: Klik ulang menu sidebar mereset state List

25. Ketik Search `Sejahtera`, tekan Enter
26. Klik header kolom Quantity sekali (ascending)
27. Ketik `2` pada input nomor halaman, tekan Enter
28. Verifikasi tabel berada di halaman 2
29. Klik ulang menu Allocation > Device Allocation dari sidebar
30. Verifikasi Search direset (kotak Search kosong)
31. Verifikasi Sort direset (indikator sort hilang)
32. Verifikasi urutan tabel kembali ke Last Updated terbaru lebih dulu dengan baris teratas `HALC-20260909-00003`
33. Verifikasi Filter tidak aktif (tidak ada badge titik pada ikon Filter)
34. Verifikasi paginasi direset ke halaman 1
35. Verifikasi tabel menampilkan 30 baris (tiga halaman)

### TC-AC-ACHA-369: State List hilang setelah logout dan login

36. Ketik Search `Budi`, tekan Enter
37. Logout dari akun aktor
38. Login dengan akun aktor Total Control Principal `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`
39. Buka Allocation > Device Allocation
40. Verifikasi state dibuang: tabel menampilkan default tanpa Search (30 baris pada tiga halaman)

## Notes

- Ukuran spec (di atas 35 langkah): tiga TC state List satu topik memakai satu dataset; tiap kontrol (Search, Filter, Sort, Page size) diverifikasi sendiri (S-01), ditambah pemulihan state antar TC.
- Sumber TC: `admin-console/device-allocation/TestCases/tc-device-allocation.md` (bagian 4a-8). Seluruh TC primer spec ini (TC-AC-ACHA-366, 367, 369) dikerjakan di sini.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): menutup Filter Panel dengan klik ikon Filter (langkah 4 dan 22); pemulihan state di akhir TC-AC-ACHA-366 (Search, Filter, Sort, Page size); Logout dan Login ulang akun aktor di TC-AC-ACHA-369 sebagai langkah ganti sesi eksplisit (TC-AC-ACHA-369 paling akhir karena Logout; hook `after` mengembalikan sesi ke akun default suite).
- Asersi tambahan (S-03): TC-AC-ACHA-367 memuat `Verifikasi` tabel di halaman 2 sebelum klik sidebar (supaya reset halaman bermakna).
- Temuan untuk QA:
  - TC-AC-ACHA-367 langkah uji pertama ("Search `Budi` lalu Enter, Sort Quantity ascending, pindah ke halaman 2") tidak dapat dijalankan: Search `Budi` hanya 6 baris (satu halaman pada Page size 10). Spec memakai Search `Sejahtera` (16 baris, dua halaman).
  - TC-AC-ACHA-367 Expected menyebut Filter direset, tetapi langkah uji tidak mengatur Filter; spec mengasersi Filter tidak aktif tanpa mengaturnya lebih dulu.
  - TC-AC-ACHA-366 Expected a ("state tidak berubah") dan b tidak menyebut cara membuka modal Allocation Log; spec memakai klik Allocation ID (TC-AC-ACHA-29).
