---
id: TC-AC-DS-E2E-150-log-request-api-langsung-aktor-berhak
title: "Request API Langsung oleh Aktor Berhak Menulis Log Tiga Surface yang Sama dengan Form"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-494
  - TC-AC-DS-583
  - TC-AC-DS-584
coverage:
  web: automated
---

# Request API Langsung oleh Aktor Berhak Menulis Log Tiga Surface yang Sama dengan Form

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Klien HTTP dengan token `Jane Setiawan` (sesi API aktor, login API password dengan `Spectra.env.AC_DS_TC_PASSWORD`, bukan sesi web; disediakan tim BE/FE) untuk request langsung ke server pada langkah 2, 17, dan 32. ID Device SKU `HHR-ARC-200` dan `TAG-ARC-OBJ` serta ID Device Name `Asset TAG` dan Brand `Arcturus` dibaca lewat fixture BE (disediakan tim BE/FE; tidak ada endpoint pembaca yang dikarang).
- Data Pre-setup: SKU inti `HHR-ARC-200` (Model/Type `H200`) dan `TAG-ARC-OBJ` (stok 0) serta seed (#29, #30), pohon Category (#25), Device Name `Asset TAG` (#26), Brand `Arcturus` (#27), file foto uji `foto-a.jpg` (#37), General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: SKU `API-LOG-01` (Device Name `Asset TAG`, Category Asset TAG, Brand `Arcturus`, Model/Type `T-AP1`, foto `foto-a.jpg`) dibuat lewat request POST pada TC-AC-DS-494 (kode literal sesuai TC; lihat Temuan untuk QA). Hook `before` menghapus `API-LOG-01` bila ada, hook `after` menghapusnya.
- Data yang diubah (target aksi tulis): SKU Pre-setup `HHR-ARC-200` (Model/Type `H201` pada TC-AC-DS-583) dan `TAG-ARC-OBJ` (dihapus pada TC-AC-DS-584). TC menetapkan baris ini sebagai Pre-setup bersama; pemulihan ke `H200` dan mendaftarkan kembali `TAG-ARC-OBJ` dijamin fixture BE (disediakan tim FE/BE) di hook `before` dan `after`, termasuk penghapusan entri Changelog yang ditambahkan spec agar Pre-setup #33 kembali 35 entri.
- Kemampuan teknis (disediakan tim FE/BE): pemulihan data di atas; pembacaan jumlah entri (baseline) Changelog Principal, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action sebelum request (audit trail permanen; 8b butir 10); pembacaan state data (nilai Model/Type, keberadaan SKU) lewat fixture BE.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-583: Request API PATCH oleh aktor berhak menulis log tiga surface yang sama dengan Edit lewat form

1. Catat baseline jumlah entri Changelog Principal, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action
2. Kirim request `PATCH /v2/enterprise-management/device-skus/{id}` (multipart/form-data) untuk Device SKU `HHR-ARC-200` lewat klien HTTP dengan token `Jane Setiawan`, dengan `model` `H201` dan formulir Edit lengkap (`sku`, `deviceNameId`, `brandId`, `model`, `defaultImage` berisi nilai tersimpan kecuali field yang disebut), hingga perubahan tersimpan
3. Verifikasi respons request berstatus 200 dengan message `Device SKU successfully updated`
4. Verifikasi Model/Type `HHR-ARC-200` menjadi `H201` (state data lewat fixture BE)
5. Muat ulang halaman
6. Klik ikon Changelog
7. Verifikasi modal "Changelog: Device SKU" tampil dengan tepat satu entri Edit baru: SKU `UHF Handheld Reader (HHR-ARC-200)`, Field `Model/Type`, Old Value `H200`, New Value `H201`, Modified By `Jane S` (jumlah entri bertambah tepat 1 dari baseline langkah 1)
8. Buka Settings > User, cari user `totalControlSku_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
9. Verifikasi System Log `Jane Setiawan` memuat entri Action `Edit`, Object `Device SKU`, Name `HHR-ARC-200`, Field `Model/Type`, Old Value `H200`, New Value `H201`
10. Buka Activity Log, buka tab User Action
11. Verifikasi Activity Log memuat entri Action `Edit`, Object `Device SKU`, Name `UHF Handheld Reader (HHR-ARC-200)`, Field `Model/Type`, Old Value `H200`, New Value `H201`, Modified By `Jane S`

### Pemulihan state antar TC

12. Buka Settings > Device > Device SKU; pulihkan Model/Type `HHR-ARC-200` menjadi `H200` lewat fixture BE

### TC-AC-DS-494: Request API langsung oleh aktor berhak menulis log yang sama dengan form

13. Catat baseline jumlah entri Changelog Principal, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action
14. Kirim request `POST /v2/enterprise-management/device-skus` (multipart/form-data) lewat klien HTTP dengan token `Jane Setiawan`, dengan `deviceNameId` Device Name `Asset TAG` (Category Asset TAG), `brandId` Brand `Arcturus`, `sku` `API-LOG-01`, `model` `T-AP1`, `firstImage` `foto-a.jpg`, dan `defaultImage` `firstImage`, hingga SKU tersimpan
15. Verifikasi respons request berstatus 201 dengan message `Device SKU successfully created`
16. Verifikasi SKU `API-LOG-01` tercatat (state data lewat fixture BE)
17. Muat ulang halaman
18. Klik ikon Changelog
19. Verifikasi modal "Changelog: Device SKU" tampil dengan entri Create: SKU `Asset TAG (API-LOG-01)`, Field `SKU`, Old Value `—`, New Value `Asset TAG (API-LOG-01)`, Modified By `Jane S` (jumlah entri bertambah tepat 1 dari baseline langkah 13)
20. Buka Settings > User, cari user `totalControlSku_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
21. Verifikasi System Log `Jane Setiawan` memuat entri Action `Create`, Object `Device SKU`, Name `API-LOG-01`, Field `SKU`, Old Value `—`, New Value `Asset TAG (API-LOG-01)`
22. Buka Activity Log, buka tab User Action
23. Verifikasi Activity Log memuat entri Action `Create`, Object `Device SKU`, Name `Asset TAG (API-LOG-01)`, Field `SKU`, Old Value `—`, New Value `Asset TAG (API-LOG-01)`, Modified By `Jane S`

### Pemulihan state antar TC

24. Buka Settings > Device > Device SKU

### TC-AC-DS-584: Request API DELETE oleh aktor berhak menulis log tiga surface yang sama dengan Delete lewat form

25. Catat baseline jumlah entri Changelog Principal, System Log aktor `Jane Setiawan`, dan Activity Log tab User Action
26. Kirim request `DELETE /v2/enterprise-management/device-skus` dengan `ids` berisi ID Device SKU `TAG-ARC-OBJ` (stok 0) lewat klien HTTP dengan token `Jane Setiawan`, hingga penghapusan tersimpan
27. Verifikasi respons request berstatus 200 dengan `data.results` berisi satu entri `status` `deleted` dan `reason` null untuk ID `TAG-ARC-OBJ`
28. Muat ulang halaman
29. Ketik Search `TAG-ARC-OBJ`, tekan Enter
30. Verifikasi List menampilkan "No results found" sehingga baris `TAG-ARC-OBJ` tidak ada lagi
31. Klik `(←)` pada kotak Search, lalu klik ikon Changelog
32. Verifikasi modal "Changelog: Device SKU" tampil dengan tepat satu entri Delete baru: SKU `Asset TAG (TAG-ARC-OBJ)`, Field `SKU`, Old Value `Asset TAG (TAG-ARC-OBJ)`, New Value `—`, Modified By `Jane S` (jumlah entri bertambah tepat 1 dari baseline langkah 25)
33. Buka Settings > User, cari user `totalControlSku_automated_{namaCompany}@qwertysystem.net`, buka Detail, buka tab System Log
34. Verifikasi System Log `Jane Setiawan` memuat entri Action `Delete`, Object `Device SKU`, Name `TAG-ARC-OBJ`, Field `SKU`, Old Value `Asset TAG (TAG-ARC-OBJ)`, New Value `—`
35. Buka Activity Log, buka tab User Action
36. Verifikasi Activity Log memuat entri Action `Delete`, Object `Device SKU`, Name `Asset TAG (TAG-ARC-OBJ)`, Field `SKU`, Old Value `Asset TAG (TAG-ARC-OBJ)`, New Value `—`, Modified By `Jane S`

### Pemulihan state akhir

37. Buka Settings > Device > Device SKU

## Notes

- K-1: TC kelas a (defense-in-depth) dengan Expected respons API (status respons dan state data lewat fixture BE) tetap masuk spec FE+BE walau tumpang tindih dengan `tc-settings-device-sku-backend.md`; BE mencatatnya pada tingkat endpoint. Request langsung ke server tidak melewati browser: asersinya hanya respons server dan state data (8b butir 1); pengecekan log pada Changelog, System Log, dan Activity Log adalah state data hasil request yang dibaca lewat UI, bukan perilaku FE atas respons.
- Urutan TC dalam spec: 583, 494, 584 (bukan urutan nomor); TC yang menghapus data di akhir (S-10).
- Spec berisi 37 langkah nominal, sedikit di atas sekitar 35 langkah. Alasan: tiga TC satu kelas (request API langsung dengan pencatatan log tiga surface) dan berdiri sendiri; sebagian besar langkah adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) yang menurut bagian 3 prinsip 13 tidak dihitung sebagai langkah smell.
- Langkah penghubung tanpa `Verifikasi`: langkah 1, 13, 25 (baseline, S-12), langkah 5, 17, 28 (memuat ulang agar List menampilkan data terbaru), langkah 12, 24, 37 (S-03, S-09), dan langkah 29 (Search untuk menemukan baris, R-16). Langkah 2, 14, 26 adalah pemicu request dengan "hingga ... tersimpan" (R-20).
- Expected 494 butir a dipecah menjadi langkah 15 dan 16; 584 butir a menjadi langkah 27 dan 30 (anchor absence baris: "No results found" Search, 8b butir 2).
- Temuan untuk QA:
  - S-13: TC tidak menyebut cara membaca ID Device SKU, Device Name, dan Brand untuk body request; ditulis sebagai kemampuan fixture BE yang disediakan tim FE/BE.
  - S-12: kode literal `API-LOG-01`, `HHR-ARC-200`, `TAG-ARC-OBJ` mengikuti TC tanpa suffix; pengecualian modul belum ada di Lampiran A (butuh keputusan).
  - S-06: TC mengubah dan menghapus baris Pre-setup bersama; pemulihan bergantung fixture BE yang belum ada.
  - S-13: pencarian user di Settings > User memakai email bersuffix `{namaCompany}`; TC hanya menyebut nama `Jane Setiawan`.
  - Fixture rancangan Pre-setup #33 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
