---
id: TC-GS-TAG-E2E-073-sort-kolom-teks-ikon-dan-actions
title: "Sort Registri: Kolom Teks (Siklus 3-State, Kosong di Akhir), Ikon TAG Type, dan Kolom Actions Tanpa Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-221
  - TC-GS-TAG-222
  - TC-GS-TAG-226
coverage:
  web: automated
---

# Sort Registri: Kolom Teks (Siklus 3-State, Kosong di Akhir), Ikon TAG Type, dan Kolom Actions Tanpa Sort

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sari Dewi (Pre-setup TC, Client A) `totalControl_automated_qaTeam1@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Seed Registri A Client A (DD-01 sampai DD-30; 30 baris, 4 Paired dan 26 Not Paired; Tabel Data Uji Dinamis TC). Di-seed dan direset idempotent lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme tidak didefinisikan di TC, Q-4). Identifier TAG bersifat tetap dan tanpa sufiks `{runId}` (`suite.md`, S-12). Spec hanya membaca data. Tiap kolom yang diuji punya sedikitnya dua nilai distinct pada Seed Registri A (S-11): `Device Name` (mis. `Access Card Reader`, `Zebra RFD40 Tag`), `Code`, `SKU` (`SKU-4410` sampai `SKU-GPS-01` dan kosong), `Source` (Official dan Self-Purchased), `Type` (`Object TAG`, `User TAG`, dan kosong), `TAG Type` (BLE, GPS, NFC, QR, RFID).
- General Settings: Date Format `dd/MM/yy`, 24-hour, Asia/Jakarta (default Client A); spec ini tidak mengubahnya.
- Suite serial (`parallel: false`).
- Flag Guided Tooltip registri (`guided_tooltip_seen_gs-tag-registry`) disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): Sort dikembalikan netral (urutan default Code A-Z) dan Rows per page dikembalikan ke 10.
- Tabel "Kolom teks umum" (parameter langkah 3 sampai 9): `Device Name`, `Code`, `Source`.
- Kemampuan teknis: membaca indikator sort pada header kolom dan urutan baris tabel; Rows per page 50 dipakai supaya seluruh 30 baris tampil pada satu halaman (langkah 1).

## Test Steps

### Persiapan

1. Ubah Rows per page menjadi 50 (seluruh 30 baris tampil pada satu halaman)

### TC-GS-TAG-221: Sort kolom teks (siklus 3-state)

2. Untuk setiap kolom pada tabel "Kolom teks umum" di Prerequisites, lakukan langkah 3 sampai 9
3. Klik header kolom itu (klik #1)
4. Verifikasi kolom diurutkan ascending A-Z (indikator sort dan urutan baris)
5. Verifikasi urutan alfabetis case-insensitive (collation en-US)
6. Klik header kolom itu (klik #2)
7. Verifikasi kolom diurutkan descending Z-A
8. Klik header kolom itu (klik #3)
9. Verifikasi sort netral kembali ke urutan default Code A-Z
10. Klik header `SKU` (klik #1)
11. Verifikasi `SKU` ascending berurutan `SKU-4410`, `SKU-5500`, `SKU-7710`, `SKU-8821`, `SKU-GPS-01`
12. Verifikasi urutan alfabetis case-insensitive (collation en-US) pada kolom `SKU`
13. Verifikasi baris SKU `—` berada di akhir daftar
14. Klik header `SKU` (klik #2)
15. Verifikasi `SKU` descending berurutan `SKU-GPS-01`, `SKU-8821`, `SKU-7710`, `SKU-5500`, `SKU-4410`
16. Verifikasi baris SKU `—` tetap di akhir daftar (kosong selalu di akhir di kedua arah)
17. Klik header `SKU` (klik #3)
18. Verifikasi sort netral kembali ke urutan default Code A-Z
19. Klik header `Type` (klik #1)
20. Verifikasi `Type` ascending berurutan `Object TAG`, lalu `User TAG`
21. Verifikasi urutan alfabetis case-insensitive (collation en-US) pada kolom `Type`
22. Verifikasi baris Type `—` (non-RFID) berada di akhir daftar
23. Klik header `Type` (klik #2)
24. Verifikasi baris Type `—` berada di awal daftar (descending)
25. Verifikasi urutan berikutnya `User TAG`, lalu `Object TAG`
26. Klik header `Type` (klik #3)
27. Verifikasi sort netral kembali ke urutan default Code A-Z

### TC-GS-TAG-222: Sort kolom TAG Type berdasarkan accessibility label ikon

28. Klik header `TAG Type` (klik #1)
29. Verifikasi `TAG Type` ascending berdasarkan label: `BLE`, `GPS`, `NFC`, `QR`, `RFID`
30. Klik header `TAG Type` (klik #2)
31. Verifikasi `TAG Type` descending berdasarkan label: `RFID`, `QR`, `NFC`, `GPS`, `BLE`
32. Klik header `TAG Type` (klik #3, kembali netral)

### TC-GS-TAG-226: Kolom Actions tidak punya ikon sort

33. Verifikasi header kolom paling kanan `Column Visibility (⋯)` tidak punya ikon sort
34. Klik header `Column Visibility (⋯)`
35. Verifikasi overlay Column Visibility terbuka
36. Tutup overlay Column Visibility
37. Ubah Rows per page kembali menjadi 10

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber dipertahankan (221, 222, 226). TC-GS-TAG-223, 224, 225 (kolom badge, tanggal, Last User) ada di spec `TC-GS-TAG-E2E-074-sort-kolom-badge-tanggal-dan-last-user`. Spec tidak mengubah data dan tidak menghapus apa pun.
- Panjang spec: 37 langkah tertulis (sekitar 51 langkah setelah ekspansi tiga kolom pada langkah 3 sampai 9), di atas sekitar 35 langkah setelah ekspansi. Alasan dipertahankan: seluruh blok satu topik (Sort kolom registri) pada satu dataset dan satu kelas harness biasa; langkah berulang memakai parameter di tabel Prerequisites tanpa langkah bersyarat (bagian 8b butir 7); tiap kolom diakhiri klik #3 yang mengembalikan sort ke netral sehingga tiap blok berdiri sendiri. `Verifikasi` yang diulang tetap satu per klausa. Langkah yang diulang: 3 sampai 9 (tiga iterasi: `Device Name`, `Code`, `Source`).
- `SKU` (langkah 10 sampai 18) dan `Type` (langkah 19 sampai 27) ditulis terpisah dari langkah berulang karena Expected TC memberi daftar nilai dan penempatan kosong yang berbeda per kolom. Butir b (urutan alfabetis case-insensitive) untuk `SKU` dan `Type` diasersi pada langkah 12 dan 21; langkah itu mengasersi butir b Expected TC-GS-TAG-221 per kolom.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 37 (Rows per page 50 supaya `User TAG` dan baris kosong pada kolom `Type` terlihat bersama, lalu dipulihkan), langkah 32 (mengembalikan sort ke netral), langkah 36 (menutup overlay).
- Pemisahan dari spec Search, Filter, dan Pagination registri: ukuran gabungan semua topik registri melewati batas langkah jauh (KEPUTUSAN 2026-10-21, bagian 3 prinsip 1).
- Absence ikon sort pada header Actions (langkah 33): Table Tools dan header kolom yang sudah termuat menjadi anchor permukaan (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-GS-TAG-221 butir c memakai `—` (em dash) untuk SKU kosong, sedangkan tabel Seed Registri A memakai `-`; spec mengikuti Expected TC. Perlu konfirmasi karakter kosong yang ditampilkan di sel.
  - TC-GS-TAG-221 tidak menyebut ukuran halaman; `Type` ascending menempatkan 22 baris `Object TAG` sebelum `User TAG` dan baris kosong, sehingga pada ukuran halaman 10 hanya `Object TAG` yang terlihat. Spec menaikkan Rows per page menjadi 50 (langkah 1).
  - TC-GS-TAG-221 langkah 2 ("Ulangi untuk `Code`...") tidak menyebut apakah klik ketiga dilakukan di tiap kolom sebelum pindah kolom; spec menyelesaikan siklus tiga klik per kolom.
  - TC-GS-TAG-222 mengurutkan berdasarkan accessibility label ikon; Expected hanya menyebut urutan label tanpa menyebut klik ketiga (netral). Langkah 32 adalah langkah penghubung.
  - Hitungan baris bergantung pada Seed Registri A utuh dan suite serial (Q-4).
