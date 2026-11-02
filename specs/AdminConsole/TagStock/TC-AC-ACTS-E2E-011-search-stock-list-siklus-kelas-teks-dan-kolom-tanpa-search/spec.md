---
id: TC-AC-ACTS-E2E-011-search-stock-list-siklus-kelas-teks-dan-kolom-tanpa-search
title: "Search Stock List: Siklus Toolbar, Kelas Teks, dan Kolom Photo/Last Updated Tanpa Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-41
  - TC-AC-ACTS-42
  - TC-AC-ACTS-46
coverage:
  web: automated
---

# Search Stock List: Siklus Toolbar, Kelas Teks, dan Kolom Photo/Last Updated Tanpa Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup #1 (akun Total Control) dan Stock List terisi minimal 5 SKU dari RFID, NFC, BLE, dan GPS dengan nilai beragam pada tiap kolom (#12 sampai #15 dan SKU pendukung).
- Spec read-only: tidak membuat, mengubah, atau menghapus data.
- Kemampuan teknis: membaca placeholder dan fokus input (kemampuan standar kerangka).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-41: Siklus Search toolbar

1. Catat jumlah baris tabel sebelum Search
2. Hover icon Search
3. Verifikasi Tooltip `Search` tampil
4. Klik icon Search
5. Verifikasi Input terbuka dengan fokus otomatis
6. Verifikasi Placeholder `Search by device name, SKU, or brand...`
7. Ketik `rfid` tanpa menekan Enter
8. Verifikasi Tabel belum tersaring (jumlah baris sama dengan sebelum Search)
9. Verifikasi Icon (✕) muncul di dalam input
10. Tekan Enter
11. Verifikasi Tabel tersaring sesuai keyword `rfid` (sedikitnya satu baris tampil)
12. Klik icon (✕) pada input
13. Verifikasi Input kosong dan kursor tetap fokus
14. Verifikasi Tabel masih menampilkan hasil search terakhir
15. Tekan Enter pada input kosong
16. Verifikasi Tabel kembali ke semua data
17. Ketik `rfid`, tekan Enter, lalu klik icon panah (←)
18. Verifikasi Kotak pencarian tertutup dan keyword dikosongkan
19. Verifikasi Tabel langsung kembali ke semua data

### TC-AC-ACTS-42: Search kelas teks Device Name dan SKU

20. Klik icon Search, ketik `rfid asset`, tekan Enter
21. Verifikasi Baris Device Name `RFID Asset Tag` tampil
22. Ganti isi kotak search dengan `RFID ASSET`, tekan Enter
23. Verifikasi Baris Device Name `RFID Asset Tag` tampil (huruf besar/kecil dibalik)
24. Ganti isi kotak search dengan `zzz-tidak-ada-dev`, tekan Enter
25. Verifikasi Empty state `No results found` tampil
26. Ganti isi kotak search dengan `asset-core`, tekan Enter
27. Verifikasi Baris SKU `RFID-ASSET-CORE-R5` tampil
28. Ganti isi kotak search dengan `ASSET-CORE`, tekan Enter
29. Verifikasi Baris SKU `RFID-ASSET-CORE-R5` tampil (huruf besar/kecil dibalik)
30. Ganti isi kotak search dengan `zzz-tidak-ada-sku`, tekan Enter
31. Verifikasi Empty state `No results found` tampil

### TC-AC-ACTS-46: Search tidak mencari kolom Photo dan Last Updated

32. Klik `(←)` pada kotak Search
33. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
34. Catat nilai Last Updated baris SKU `Fixture.tagStock.skuRfid`
35. Verifikasi Kolom Last Updated baris SKU itu memuat nilai tanggal
36. Ganti isi kotak search dengan nilai Last Updated yang dicatat, tekan Enter
37. Verifikasi Empty state `No results found` tampil (tidak ada baris ditemukan dari kolom Last Updated)
38. Klik icon Filter
39. Verifikasi Filter Panel memuat field `Last Updated` (penyaringan kolom tersebut hanya lewat Filter Panel dengan Date range picker)
40. Verifikasi Filter Panel tidak memuat field `Photo` (kolom Photo tidak filterable)
41. Tutup Filter Panel

## Notes

- Sekitar 35 langkah (di atas smell, 41 langkah): semua blok satu objek uji (Search Stock List) dengan dataset sama; TC-AC-ACTS-41 sampai 46 membangun input Search berurutan sehingga satu spec menghindari pembukaan ulang halaman.
- Langkah penghubung (S-03): `(←)` pada kotak Search mengosongkan dan menutup input sebelum TC berikutnya (S-09); menutup Filter Panel.
- Temuan untuk QA (S-15): TC-AC-ACTS-46 butir b menyebut kolom Photo "tidak searchable" tanpa nilai yang dapat diketik; spec hanya mengasersi bahwa field Photo tidak ada di Filter Panel dan Search nilai Last Updated tidak menemukan baris. TC-AC-ACTS-41 butir d menyebut tabel "masih menampilkan hasil search terakhir" tanpa angka; spec mengasersi tidak ada perubahan dari hasil sebelumnya.
