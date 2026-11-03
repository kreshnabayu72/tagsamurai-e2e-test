---
id: TC-AC-DS-E2E-146-log-tiga-surface-delete-bulk-delete-dan-edit-multi-field
title: "Log Tiga Surface: Delete Single, Bulk Delete, dan Edit Beberapa Field Sekaligus"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-479
  - TC-AC-DS-480
  - TC-AC-DS-481
coverage:
  web: automated
---

# Log Tiga Surface: Delete Single, Bulk Delete, dan Edit Beberapa Field Sekaligus

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: SKU inti `HHR-ARC-100` (stok 120, dilewati Bulk Delete), `HHR-ARC-200` (stok 0; Model/Type `H200`, Brand `Arcturus`, Range Type `Short Range`), `TAG-ARC-OBJ` (stok 0), seed `SEED-005` (#30) serta seed (#29), pohon Category (#25), Device Name (#26), Brand Principal `Arcturus`, `Kinetia` (#27), General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35), riwayat Changelog Principal (#33). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data yang diubah (target aksi tulis): SKU Pre-setup `HHR-ARC-200` (Model/Type `H202`, Brand `Kinetia`, Range Type `Long Range` pada TC-AC-DS-481; dihapus pada TC-AC-DS-480), `TAG-ARC-OBJ` (dihapus pada TC-AC-DS-479), dan `SEED-005` (dihapus pada TC-AC-DS-480). TC menetapkan baris ini sebagai Pre-setup bersama (nilai Expected bergantung pada kodenya); pemulihan data ke keadaan awal (termasuk mendaftarkan kembali ketiga SKU yang dihapus dan menghapus entri Changelog yang ditambahkan spec agar Pre-setup #33 kembali 35 entri) dijamin fixture BE (disediakan tim FE/BE) di hook `before`, di antara TC (langkah 17), dan di hook `after`. Efek: total SKU Principal 129 berkurang selama spec dan Last Modified `HHR-ARC-200` berubah.
- Kemampuan teknis (disediakan tim FE/BE): pemulihan data di atas; pembacaan jumlah entri (baseline) Changelog Principal, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action sebelum dan sesudah aksi (audit trail permanen; 8b butir 10); jam server dan jam browser sinkron untuk asersi Date.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-481: Edit beberapa field sekaligus menghasilkan satu entri per field yang berubah tanpa duplikat dan tanpa entri nyasar

1. Catat baseline jumlah entri Changelog Principal, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action
2. Ketik Search `HHR-ARC-200`, tekan Enter
3. Klik ⋯ pada baris `HHR-ARC-200`, pilih `Edit`
4. Verifikasi Popup Edit SKU tampil dengan field terisi
5. Ubah Model/Type menjadi `H202`, Brand menjadi `Kinetia`, dan Range Type menjadi `Long Range`; biarkan Port, Device Name, dan SKU tidak berubah
6. Klik `[Save]`
7. Tunggu aksi selesai: Popup Edit SKU tertutup
8. Klik ikon Changelog
9. Verifikasi modal "Changelog: Device SKU" tampil dengan tiga entri Edit baru untuk `UHF Handheld Reader (HHR-ARC-200)`: Field `Model/Type` (`H200` > `H202`), `Brand` (`Arcturus` > `Kinetia`), dan `Range Type` (`Short Range` > `Long Range`)
10. Verifikasi jumlah entri Changelog bertambah tepat 3 dari baseline langkah 1 (tidak ada entri ganda untuk field yang sama dan tidak ada entri untuk field yang tidak berubah)
11. Verifikasi ketiga entri baru seluruhnya memuat SKU `UHF Handheld Reader (HHR-ARC-200)` (tidak ada entri yang menyasar SKU lain)
12. Buka Settings > User, cari user `totalControlSku_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
13. Verifikasi System Log aktor `Jane Setiawan` memuat tiga entri Edit yang sama untuk Name `HHR-ARC-200` (jumlah entri bertambah tepat 3 dari baseline langkah 1)
14. Buka Activity Log, buka tab User Action
15. Verifikasi Activity Log tab User Action memuat tiga entri Edit yang sama untuk Name `UHF Handheld Reader (HHR-ARC-200)` (jumlah entri bertambah tepat 3 dari baseline langkah 1)

### Pemulihan state antar TC

16. Buka Settings > Device > Device SKU
17. Pulihkan `HHR-ARC-200` (Model/Type `H200`, Brand `Arcturus`, Range Type `Short Range`) lewat fixture BE

### TC-AC-DS-479: Log Delete SKU single: Old berisi Device Name dan kode dan New strip

18. Catat baseline jumlah entri Changelog Principal, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action
19. Ketik Search `TAG-ARC-OBJ`, tekan Enter
20. Klik ⋯ pada baris `TAG-ARC-OBJ`, pilih `Delete`
21. Verifikasi dialog Delete tampil
22. Klik `[Delete]`
23. Tunggu aksi selesai: dialog tertutup
24. Catat waktu aksi
25. Klik ikon Changelog
26. Verifikasi modal "Changelog: Device SKU" tampil dengan entri baru Action `Delete`, SKU `Asset TAG (TAG-ARC-OBJ)`, Field `SKU`, Old Value `Asset TAG (TAG-ARC-OBJ)`, New Value `—`, Modified By `Jane S` di baris pertama
27. Verifikasi Date entri itu sesuai waktu aksi menurut General Settings (toleransi satu menit)
28. Buka Settings > User, cari user `totalControlSku_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
29. Verifikasi System Log aktor `Jane Setiawan` memuat entri Action `Delete`, Object `Device SKU`, Name `TAG-ARC-OBJ`, Field `SKU`, Old Value `Asset TAG (TAG-ARC-OBJ)`, New Value `—`
30. Buka Activity Log, buka tab User Action
31. Verifikasi Activity Log tab User Action memuat entri Action `Delete`, Object `Device SKU`, Name `Asset TAG (TAG-ARC-OBJ)`, Field `SKU`, Old Value `Asset TAG (TAG-ARC-OBJ)`, New Value `—`, Modified By `Jane S`
32. Verifikasi jumlah entri pada ketiga surface bertambah tepat 1 dari baseline langkah 18 (tidak ada entri log ganda)

### Pemulihan state antar TC

33. Buka Settings > Device > Device SKU

### TC-AC-DS-480: Log Bulk Delete: satu entri Delete per SKU terhapus dan SKU yang dilewati tidak dicatat

34. Catat baseline jumlah entri Changelog Principal, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action
35. Centang baris `HHR-ARC-100`, `HHR-ARC-200`, dan `SEED-005`
36. Pilih Bulk Action > Delete
37. Verifikasi dialog Bulk Delete tampil
38. Klik `[Continue]`
39. Tunggu aksi selesai: dialog tertutup
40. Klik ikon Changelog
41. Verifikasi modal "Changelog: Device SKU" tampil dengan dua entri Delete baru: `UHF Handheld Reader (HHR-ARC-200)` dan `Seed Tag (SEED-005)`, masing-masing Field `SKU`, Old Value berformat Device Name dan kode, New Value `—`
42. Verifikasi jumlah entri Changelog bertambah tepat 2 dari baseline langkah 34 sehingga tidak ada entri untuk `HHR-ARC-100` yang dilewati karena masih berstok
43. Buka Settings > User, cari user `totalControlSku_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
44. Verifikasi System Log aktor `Jane Setiawan` memuat dua entri Delete yang sama (jumlah entri bertambah tepat 2 dari baseline langkah 34)
45. Buka Activity Log, buka tab User Action
46. Verifikasi Activity Log tab User Action memuat dua entri Delete yang sama (jumlah entri bertambah tepat 2 dari baseline langkah 34)

### Pemulihan state akhir

47. Buka Settings > Device > Device SKU

## Notes

- Spec berisi 47 langkah nominal, melewati sekitar 35 langkah. Alasan: tiga TC satu kelas (pencatatan log tiga surface) dan berdiri sendiri; sebagian besar langkah adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log; langkah 8 sampai 15, 25 sampai 32, 40 sampai 46) yang menurut bagian 3 prinsip 13 tidak dihitung sebagai langkah smell. Kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Urutan TC dalam spec: 481, 479, 480 (bukan urutan nomor); TC yang menghapus data diletakkan di akhir dan Bulk Delete terakhir (S-10). Pemulihan `HHR-ARC-200` di langkah 17 menjaga keadaan awal TC-AC-DS-480.
- Langkah penghubung tanpa `Verifikasi`: langkah 1, 18, 34 (baseline, S-12), langkah 2 dan 19 (Search untuk menemukan baris target, R-16), langkah 24 (mencatat waktu aksi), langkah 16, 17, 33, 47 (S-03, S-09). Langkah 35 mencentang baris tanpa Search.
- Expected 480 butir b ("tidak ada entri untuk `HHR-ARC-100`") ditulis sebagai asersi jumlah berbaseline (langkah 42), bukan asersi absence kelas g (bagian 3 prinsip 13 butir g). Expected 481 butir b dan d dipecah menjadi langkah 10 dan 11.
- Temuan untuk QA:
  - S-12: nilai literal Pre-setup (`HHR-ARC-100`, `HHR-ARC-200`, `TAG-ARC-OBJ`, `SEED-005`) mengikuti TC tanpa suffix; pengecualian modul belum ada di Lampiran A (butuh keputusan).
  - S-06: TC menghapus dan mengubah baris Pre-setup bersama; pemulihan (mendaftarkan kembali SKU terhapus, menghapus entri audit trail) bergantung fixture BE yang belum ada.
  - S-14: TC 480 langkah 2 mencentang tiga baris tanpa menyebut bagaimana ketiganya dijangkau (halaman atau Search berbeda); spec mengikuti TC dan mengandalkan seleksi lintas halaman.
  - S-13: pencarian user di Settings > User memakai email bersuffix `{namaCompany}`; TC hanya menyebut nama `Jane Setiawan`.
  - Fixture rancangan Pre-setup #33 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
