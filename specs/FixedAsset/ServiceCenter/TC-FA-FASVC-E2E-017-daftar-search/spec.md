---
id: TC-FA-FASVC-E2E-017-daftar-search
title: "Daftar Service Center: Search per Kolom, Substring, Spasi, dan Tanpa Hasil"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["S-FASVC-03", "EB-SRC-1", "EB-SRC-2@tabel-service-center", "EB-SRC-3@tabel-service-center"]
smoke: []
dependsOn: []
trace:
  "S-FASVC-03": [27, 32, 39]
  "EB-SRC-1": [2, 4, 6, 17, 19, 37, 39, 46, 47, 52, 53]
  "EB-SRC-2@tabel-service-center": [14, 15, 27, 44, 56]
  "EB-SRC-3@tabel-service-center": [8, 10, 12, 21, 22, 24, 25]
anchor: [55]
coverage:
  web: automated
---

# Daftar Service Center: Search per Kolom, Substring, Spasi, dan Tanpa Hasil

## Prerequisites
- Aktor: Total Control `Rina Wijaya` (cakupan seluruh Group). Aktor lain pemicu perubahan: Total Control `Dewi Santoso {runId}`.
- Layar awal: Add-ons > Service Center (halaman daftar).
- Data:
  - DU-017-1: Group `Cabang Cari Satu {runId}`, anak langsung dari root pohon Group.
  - DU-017-2: Group `Cabang Cari Dua {runId}`, anak langsung dari root pohon Group.
  - DU-017-3: Group `Cabang Cari Tiga {runId}`, anak langsung dari root pohon Group.
  - DU-017-4: Category `Generator Cari {runId}`, di pohon Category.
  - DU-017-5: Category `Kompresor Cari {runId}`, di pohon Category.
  - DU-017-6: Category `Pompa Cari {runId}`, di pohon Category.
  - DU-017-7: Brand `Kubota Cari {runId}`, status Active di master.
  - DU-017-8: Service Center `Bengkel Mitra Sentosa {runId}`, Service type `Routine` dan `Repair`, Available to `Cabang Cari Satu {runId}`, `Cabang Cari Dua {runId}`, dan `Cabang Cari Tiga {runId}`, Specialization `Generator Cari {runId}`, `Kompresor Cari {runId}`, dan `Pompa Cari {runId}`, Brands `Kubota Cari {runId}`, City `Madiun {runId}`, Status `Active`, Usage `0`.
  - DU-017-9: Service Center `Servis Cepat Barokah {runId}`, Service type `Routine`, Available to `Cabang Cari Satu {runId}`, Specialization kosong, Brands kosong, City `Madiun {runId}`, Status `Inactive`, Usage `0`.
  - DU-017-10: Service Center `Pelita 100% Jaya {runId}`, Service type `Routine`, Available to `Cabang Cari Satu {runId}`, City `Blitar`, Status `Active`, Usage `0`.
  - DU-017-11: Service Center `Pelita 100 Jaya {runId}`, Service type `Routine`, Available to `Cabang Cari Satu {runId}`, City `Blitar`, Status `Active`, Usage `0`.
  - DU-017-12: Service Center `Teknik_Ria {runId}`, Service type `Routine`, Available to `Cabang Cari Satu {runId}`, City `Blitar`, Status `Active`, Usage `0`.
  - DU-017-13: Service Center `Teknik Ria {runId}`, Service type `Routine`, Available to `Cabang Cari Satu {runId}`, City `Blitar`, Status `Active`, Usage `0`.
  - DU-017-14: Service Center `Servis Kubota Cari {runId}`, Service type `Routine`, Available to `Cabang Cari Satu {runId}`, City `Blitar`, Status `Active`, Usage `0`.
  - DU-017-15: Kata kunci Search `Zzz Cari Tidak Ada {runId}`, tidak cocok dengan nilai di kolom mana pun.
  - DU-017-16: Kata kunci Search `T0` dalam format `dd/MM/yy`, dengan `T0` adalah tanggal hari run; nilai Last Updated semua Service Center spec ini jatuh pada `T0`.
  - DU-017-17: User `Dewi Santoso {runId}`, role Total Control, cakupan seluruh Group, Status `Active`; tampil `Dewi S` pada kolom Modified By.
  - DU-017-18: Service Center `Layanan 148 Cari {runId}`, Service type `Routine`, Available to `Cabang Cari Satu {runId}`, City `Blitar`, Status `Active`, Usage `0`.
  - DU-017-19: Service Center `Bengkel Usage Cari {runId}`, Service type `Routine`, Available to `Cabang Cari Satu {runId}`, City `Blitar`, Status `Active`, Usage `148`.
- Kondisi: client memiliki lisensi addon Maintenance berstatus aktif. Date Format bernilai `dd/MM/yy`. Akun `Dewi Santoso {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Search mencocokkan substring di kolom teks tanpa membedakan huruf besar-kecil
1. Ketik Search `Servis Cepat Barokah {runId}` pada daftar, tekan Enter
2. Verifikasi baris `Servis Cepat Barokah {runId}` tampil
3. Ganti isi kotak search daftar dengan `itra Sentosa {runId}`, tekan Enter
4. Verifikasi baris `Bengkel Mitra Sentosa {runId}` tampil
5. Ganti isi kotak search daftar dengan `bengkel mitra sentosa {runId}`, tekan Enter
6. Verifikasi baris `Bengkel Mitra Sentosa {runId}` tampil

### Spasi tepi dibuang dan spasi di tengah dipertahankan
7. Ganti isi kotak search daftar dengan `Servis Cepat Barokah {runId}` yang diapit satu spasi di awal dan satu spasi di akhir, tekan Enter
8. Verifikasi baris `Servis Cepat Barokah {runId}` tampil seperti pada Search tanpa spasi tepi
9. Ganti isi kotak search daftar dengan `Mitra Sentosa {runId}`, tekan Enter
10. Verifikasi baris `Bengkel Mitra Sentosa {runId}` tampil
11. Ganti isi kotak search daftar dengan `Bengkel Sentosa {runId}`, tekan Enter
12. Verifikasi baris `Bengkel Mitra Sentosa {runId}` tampil[^drift-1]

### Search mencocokkan nilai di kolom berbeda, chip yang tersembunyi, dan kolom teks
13. Ganti isi kotak search daftar dengan `Kubota Cari {runId}`, tekan Enter
14. Verifikasi baris `Servis Kubota Cari {runId}` tampil karena kata kunci cocok di kolom Name
15. Verifikasi baris `Bengkel Mitra Sentosa {runId}` tampil karena kata kunci cocok di kolom Brands
16. Ganti isi kotak search daftar dengan `Pompa Cari {runId}`, tekan Enter
17. Verifikasi baris `Bengkel Mitra Sentosa {runId}` tampil karena kata kunci cocok dengan nilai ketiga di Specialization yang tersembunyi di balik `+1 more`
18. Ganti isi kotak search daftar dengan `Madiun {runId}`, tekan Enter
19. Verifikasi baris `Bengkel Mitra Sentosa {runId}` tampil karena kata kunci cocok di kolom City

### Karakter pola dicari sebagai teks biasa
20. Ganti isi kotak search daftar dengan `100% Jaya {runId}`, tekan Enter
21. Verifikasi baris `Pelita 100% Jaya {runId}` tampil
22. Verifikasi baris `Pelita 100 Jaya {runId}` tidak tampil
23. Ganti isi kotak search daftar dengan `k_Ria {runId}`, tekan Enter
24. Verifikasi baris `Teknik_Ria {runId}` tampil
25. Verifikasi baris `Teknik Ria {runId}` tidak tampil

### Search tidak mencakup kolom tanggal dan kolom yang disembunyikan
26. Ganti isi kotak search daftar dengan `T0` dalam format `dd/MM/yy`, tekan Enter
27. Verifikasi empty state dengan judul `No results found` tampil
28. Klik header kolom Actions (`⋯`) pada tabel daftar
29. Hilangkan centang `City` pada panel Column Visibility
30. Tekan Esc untuk menutup panel Column Visibility
31. Ganti isi kotak search daftar dengan `Madiun {runId}`, tekan Enter
32. Verifikasi empty state dengan judul `No results found` tampil
33. Klik header kolom Actions (`⋯`) pada tabel daftar
34. Centang `City` pada panel Column Visibility
35. Tekan Esc untuk menutup panel Column Visibility
36. Tekan Enter pada kotak search daftar
37. Verifikasi baris `Bengkel Mitra Sentosa {runId}` tampil kembali

### Search tanpa kecocokan menampilkan empty state hasil kosong
38. Ganti isi kotak search daftar dengan `Zzz Cari Tidak Ada {runId}`, tekan Enter
39. Verifikasi empty state dengan judul `No results found` dan keterangan `Try adjusting your search or filter.` tampil

### Search mencocokkan nilai badge, termasuk nilai yang menjadi substring nilai lain
40. Klik ikon `Filter` pada toolbar daftar
41. Pilih `Madiun {runId}` pada filter `City`
42. Klik `[Apply]`
43. Ganti isi kotak search daftar dengan `Inactive`, tekan Enter
44. Verifikasi baris `Servis Cepat Barokah {runId}` tampil karena kata kunci cocok dengan badge Status `Inactive`
45. Ganti isi kotak search daftar dengan `Active`, tekan Enter
46. Verifikasi baris `Bengkel Mitra Sentosa {runId}` tampil karena kata kunci cocok dengan badge Status `Active`
47. Verifikasi baris `Servis Cepat Barokah {runId}` tampil karena kata kunci `Active` adalah substring dari badge Status `Inactive`
48. Klik `[Clear Field]`
49. Klik `[Apply]`

### Search mencocokkan nama pengubah pada kolom Modified By
50. Pengguna `Dewi Santoso {runId}` mengubah Notes menjadi `Vendor dicek ulang` pada Service Center `Servis Kubota Cari {runId}`
51. Ganti isi kotak search daftar dengan `Dewi S`, tekan Enter
52. Verifikasi baris `Servis Kubota Cari {runId}` tampil karena kata kunci cocok di kolom Modified By
53. Verifikasi baris `Bengkel Mitra Sentosa {runId}` tidak tampil karena pengubah terakhirnya bukan `Dewi Santoso {runId}`

### Search tidak mencakup kolom Usage
54. Ganti isi kotak search daftar dengan `148`, tekan Enter
55. Verifikasi baris `Layanan 148 Cari {runId}` tampil karena kata kunci cocok di kolom Name
56. Verifikasi baris `Bengkel Usage Cari {runId}` tidak tampil karena Usage `148` tidak ikut dicari

[^drift-1]: Drift PRD vs kontrak. PRD §5: «Search submit Enter, mencari kolom yang tampil dan bertanda Searchable (§4.1a), tanpa membedakan huruf besar-kecil», dan foundation `prd-conventions.md` §9.16: «query tidak dipecah menjadi beberapa kata». Kontrak `SearchButton#5`: «A row matches when one of its values contains the whole query as a case-insensitive substring, or when every whitespace-separated word of the query appears somewhere in the row's values (any order, words may sit in different columns).» Diasersi: kontrak `SearchButton#5`, karena kedua bunyi tidak bisa berlaku bersama (SB-7).
