---
id: TC-AC-DS-E2E-144-log-tiga-surface-edit-port-user-tag-dan-photo
title: "Log Tiga Surface: Edit Port, User TAG, dan Photo Satu Foto"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-473
  - TC-AC-DS-474
  - TC-AC-DS-475
coverage:
  web: automated
---

# Log Tiga Surface: Edit Port, User TAG, dan Photo Satu Foto

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: SKU inti `SFR-ZERO-01` (Device Name `Tunnel Scanner`, Port `9090`), `TAG-ARC-OBJ` (Device Name `Asset TAG`, TAG Type `Object`), `HHR-ARC-100` (2 foto, foto kedua default) serta seed (#29, #30), pohon Category (#25), Device Name (#26), Brand Principal (#27), file foto uji `foto-c.jpeg` (#37), General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35), riwayat Changelog Principal (#33). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data yang diubah (target aksi tulis): SKU Pre-setup `SFR-ZERO-01` (Port `9090` menjadi `9100`, TC-AC-DS-473), `TAG-ARC-OBJ` (`This is User TAG` dicentang sehingga TAG Type `Object` menjadi `User`, TC-AC-DS-474), dan `HHR-ARC-100` (foto kedua diganti `foto-c.jpeg`, TC-AC-DS-475). TC menetapkan baris ini sebagai Pre-setup bersama; pemulihan ke Port `9090`, TAG Type `Object`, dan foto kedua semula (default tetap pada foto kedua) dijamin fixture BE (disediakan tim FE/BE) di hook `before` dan `after`, termasuk penghapusan entri Changelog yang ditambahkan spec agar Pre-setup #33 kembali 35 entri. Efek: Last Modified ketiga SKU berubah.
- Kemampuan teknis (disediakan tim FE/BE): pemulihan data di atas; pembacaan jumlah entri (baseline) Changelog Principal, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action sebelum dan sesudah aksi (audit trail permanen; 8b butir 10); jam server dan jam browser sinkron untuk asersi Date.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-473: Log Edit Port

1. Catat baseline jumlah entri Changelog Principal, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action
2. Ketik Search `SFR-ZERO-01`, tekan Enter
3. Klik ⋯ pada baris `SFR-ZERO-01`, pilih `Edit`
4. Verifikasi Popup Edit SKU tampil dengan field terisi
5. Ubah Port dari `9090` menjadi `9100`
6. Klik `[Save]`
7. Tunggu aksi selesai: Popup Edit SKU tertutup
8. Catat waktu aksi
9. Klik ikon Changelog
10. Verifikasi modal "Changelog: Device SKU" tampil dengan entri baru Action `Edit`, SKU `Tunnel Scanner (SFR-ZERO-01)`, Field `Port`, Old Value `9090`, New Value `9100`, Modified By `Jane S` di baris pertama
11. Verifikasi Date entri itu sesuai waktu aksi menurut General Settings (toleransi satu menit)
12. Buka Settings > User, cari user `totalControlSku_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
13. Verifikasi System Log aktor `Jane Setiawan` memuat entri Action `Edit`, Object `Device SKU`, Name `SFR-ZERO-01`, Field `Port`, Old Value `9090`, New Value `9100`
14. Buka Activity Log, buka tab User Action
15. Verifikasi Activity Log tab User Action memuat entri Action `Edit`, Object `Device SKU`, Name `Tunnel Scanner (SFR-ZERO-01)`, Field `Port`, Old Value `9090`, New Value `9100`, Modified By `Jane S`
16. Verifikasi jumlah entri pada ketiga surface bertambah tepat 1 dari baseline langkah 1 (tidak ada entri log ganda)

### Pemulihan state antar TC

17. Buka Settings > Device > Device SKU

### TC-AC-DS-474: Log Edit User TAG memakai nilai Object atau User

18. Catat baseline jumlah entri Changelog Principal, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action
19. Ketik Search `TAG-ARC-OBJ`, tekan Enter
20. Klik ⋯ pada baris `TAG-ARC-OBJ`, pilih `Edit`
21. Verifikasi Popup Edit SKU tampil dengan field terisi
22. Centang checkbox `This is User TAG`
23. Klik `[Save]`
24. Tunggu aksi selesai: Popup Edit SKU tertutup
25. Catat waktu aksi
26. Klik ikon Changelog
27. Verifikasi modal "Changelog: Device SKU" tampil dengan entri baru Action `Edit`, SKU `Asset TAG (TAG-ARC-OBJ)`, Field `User TAG`, Old Value `Object`, New Value `User`, Modified By `Jane S` di baris pertama
28. Verifikasi Date entri itu sesuai waktu aksi menurut General Settings (toleransi satu menit)
29. Buka Settings > User, cari user `totalControlSku_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
30. Verifikasi System Log aktor `Jane Setiawan` memuat entri Action `Edit`, Object `Device SKU`, Name `TAG-ARC-OBJ`, Field `User TAG`, Old Value `Object`, New Value `User`
31. Buka Activity Log, buka tab User Action
32. Verifikasi Activity Log tab User Action memuat entri Action `Edit`, Object `Device SKU`, Name `Asset TAG (TAG-ARC-OBJ)`, Field `User TAG`, Old Value `Object`, New Value `User`, Modified By `Jane S`
33. Verifikasi jumlah entri pada ketiga surface bertambah tepat 1 dari baseline langkah 18 (tidak ada entri log ganda)

### Pemulihan state antar TC

34. Buka Settings > Device > Device SKU

### TC-AC-DS-475: Log Edit Photo mengganti satu foto: satu entri dengan Old dan New strip

35. Catat baseline jumlah entri Changelog Principal, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action
36. Ketik Search `HHR-ARC-100`, tekan Enter
37. Klik ⋯ pada baris `HHR-ARC-100`, pilih `Edit`
38. Verifikasi Popup Edit SKU tampil dengan field terisi
39. Ganti foto kedua dengan mengunggah `foto-c.jpeg`
40. Klik `[Save]`
41. Tunggu aksi selesai: Popup Edit SKU tertutup
42. Catat waktu aksi
43. Klik ikon Changelog
44. Verifikasi modal "Changelog: Device SKU" tampil dengan entri baru Action `Edit`, SKU `UHF Handheld Reader (HHR-ARC-100)`, Field `Photo`, Old Value `—`, New Value `—`, Modified By `Jane S` di baris pertama
45. Verifikasi Date entri itu sesuai waktu aksi menurut General Settings (toleransi satu menit)
46. Buka Settings > User, cari user `totalControlSku_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
47. Verifikasi System Log aktor `Jane Setiawan` memuat entri Action `Edit`, Object `Device SKU`, Name `HHR-ARC-100`, Field `Photo`, Old Value `—`, New Value `—`
48. Buka Activity Log, buka tab User Action
49. Verifikasi Activity Log tab User Action memuat entri Action `Edit`, Object `Device SKU`, Name `UHF Handheld Reader (HHR-ARC-100)`, Field `Photo`, Old Value `—`, New Value `—`, Modified By `Jane S`
50. Verifikasi jumlah entri pada ketiga surface bertambah tepat 1 dari baseline langkah 35 (tidak ada entri `Photo — Set as default` karena tanda default tetap pada foto semula)

### Pemulihan state akhir

51. Buka Settings > Device > Device SKU

## Notes

- Spec berisi 51 langkah nominal, melewati sekitar 35 langkah. Alasan: tiga TC satu kelas (pencatatan log tiga surface) dan berdiri sendiri; sebagian besar langkah adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log; langkah 9 sampai 16, 26 sampai 33, 43 sampai 50) yang menurut bagian 3 prinsip 13 tidak dihitung sebagai langkah smell. Kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Langkah penghubung tanpa `Verifikasi`: langkah 1, 18, 35 (baseline, S-12), langkah 2, 19, 36 (Search untuk menemukan baris target, R-16), langkah 8, 25, 42 (mencatat waktu aksi), dan langkah 17, 34, 51 (kembali ke List, S-03, S-09).
- Expected tiap TC butir a dipecah: kolom entri Changelog dalam satu `Verifikasi` dan Date terpisah; butir b dan c satu `Verifikasi` per surface. Expected 475 butir d ("tidak ada entri `Photo — Set as default`") ditulis sebagai asersi jumlah berbaseline (langkah 50), bukan asersi absence kelas g (bagian 3 prinsip 13 butir g).
- Temuan untuk QA:
  - S-12: nilai literal Pre-setup (`SFR-ZERO-01`, `TAG-ARC-OBJ`, `HHR-ARC-100`) mengikuti TC tanpa suffix; pengecualian modul belum ada di Lampiran A (butuh keputusan).
  - S-06: TC mengubah baris Pre-setup bersama; pemulihan (termasuk penghapusan entri audit trail permanen) bergantung fixture BE yang belum ada.
  - S-15: TC 475 langkah 3 ("ganti foto kedua dengan mengunggah foto-c.jpeg") tidak menyebut cara mengganti foto (hapus lalu unggah atau timpa); ditulis apa adanya.
  - S-13: pencarian user di Settings > User memakai email bersuffix `{namaCompany}`; TC hanya menyebut nama `Jane Setiawan`.
  - Fixture rancangan Pre-setup #33 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
