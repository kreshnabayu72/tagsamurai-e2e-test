---
id: TC-AC-DN-E2E-057-edit-ubah-banyak-field-dan-device-name-ber-sku
title: "Edit Device Name: Ubah Tiga Field, Device Name ber-SKU (Nama, Measurement, Category), dan Category node Induk"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-132
  - TC-AC-DN-133
  - TC-AC-DN-588
  - TC-AC-DN-157
  - TC-AC-DN-158
coverage:
  web: automated
---

# Edit Device Name: Ubah Tiga Field, Device Name ber-SKU (Nama, Measurement, Category), dan Category node Induk

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap yang dirujuk spec: email akun Pre-setup #1, Measurement master `Unit`, `Meter`, `Box`, serta nama node pohon Category. Nama record dinamis dibentuk `<nama dasar> {runId}-057` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja, tidak diubah): #13 Measurement `Unit`, `Meter`, `Box`; #14 Pohon Category (`Hardware` > `Smart Fixed Reader` > `Antenna`; `Hardware` > `Handheld Reader` > `UHF Handheld`; `TAG` > `NFC` > `Accessory`, `Tag`); #20 General Settings (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). #15 Brand `Brand A`, `Brand B`, `Brand C`. Record inti Pre-setup #16 tidak menjadi target aksi; target aksi memakai record milik spec di bawah (S-06).
- Data Dinamis (milik spec; dibuat lewat API di hook `before`, dihapus di hook `after` termasuk hasil rename; kemampuan seeding Device Name disediakan tim FE/BE). Last Modified record seed berisi waktu pembuatan karena belum ada entri Changelog.

  | Kode | Nama awal | Measurement | Category | SKU | Dipakai oleh |
  |---|---|---|---|---|---|
  | R1 | `Door Antenna {runId}-057` | `Unit` | `Antenna` | tanpa SKU | TC-AC-DN-132 |
  | R2 | `RFID Reader {runId}-057` | `Unit` | `UHF Handheld` | tiga SKU: `Brand A`/`Model R1`, `Brand B`/`Model R2`, `Brand C`/`Model R3` | TC-AC-DN-133 |
  | R3 | `RFID Scanner {runId}-057` | `Unit` | `UHF Handheld` | tiga SKU seperti R2 | TC-AC-DN-158, TC-AC-DN-588 |
  | R4 | `Door Induk {runId}-057` | `Unit` | `Antena Uji {runId}-057` | tanpa SKU | TC-AC-DN-157 |

- Category uji milik spec: node leaf `Antena Uji {runId}-057` dibuat fixture di bawah `Hardware` > `Smart Fixed Reader` sebagai kategori tersimpan R4; sebelum TC-AC-DN-157 fixture menambahkan Subcategory `Antena Outdoor {runId}-057` di bawahnya sehingga kategori tersimpan R4 menjadi node induk (peran admin lain di TC). Kedua node dihapus di hook `after`. Pohon Pre-setup #14 (`Antenna` tetap leaf) tidak diubah.
- Kemampuan teknis: seeding SKU Brand/Model untuk Device Name, fixture backend untuk membuat dan menghapus node Category uji, serta mengetik dan memilih opsi dropdown dan node pohon Category.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Search `{runId}-057` yang aktif sepanjang spec dipulihkan (dikosongkan) bila langkah berikutnya bergantung pada daftar penuh.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Ketik Search `{runId}-057`, tekan Enter

### TC-AC-DN-158: Edit Category pada Device Name yang masih punya SKU

2. Buka menu aksi pada baris `RFID Scanner {runId}-057`, klik `Edit`
3. Klik field Category lalu pilih leaf `Antenna`
4. Klik `[Save]`
5. Verifikasi error inline di bawah field Category "This device name already has SKUs. Category cannot be changed."
6. Verifikasi popup form tetap terbuka
7. Verifikasi tidak ada toast
8. Klik icon close `[✕]` pada popup
9. Verifikasi dialog `Unsaved Changes` tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" serta tombol `[Cancel]` dan `[Leave]`
10. Klik `[Leave]` pada dialog
11. Verifikasi baris `RFID Scanner {runId}-057` menampilkan Category badge `UHF Handheld`

### TC-AC-DN-157: Category tersimpan berubah menjadi node induk

12. Buka menu aksi pada baris `Door Induk {runId}-057`, klik `Edit`
13. Verifikasi field Category menampilkan `Antena Uji {runId}-057` apa adanya
14. Verifikasi tidak ada pesan error saat popup dibuka
15. Klik `[Save]`
16. Verifikasi toast netral "No changes to save."
17. Verifikasi popup form tertutup
18. Verifikasi baris `Door Induk {runId}-057` menampilkan Category badge `Antena Uji {runId}-057`

### TC-AC-DN-132: Edit mengubah Device Name, Measurement, dan Category sekaligus

19. Buka menu aksi pada baris `Door Antenna {runId}-057`, klik `Edit`
20. Kosongkan field Device Name lalu ketik "Hall Reader {runId}-057"
21. Klik field Measurement lalu pilih `Box`
22. Klik field Category, expand `Hardware` lalu `Handheld Reader`, pilih leaf `UHF Handheld`
23. Klik `[Save]`
24. Verifikasi toast sukses "Success, device name has been updated."
25. Verifikasi baris `Hall Reader {runId}-057` tampil di List
26. Verifikasi baris `Hall Reader {runId}-057` menampilkan Category badge `UHF Handheld`
27. Verifikasi baris `Hall Reader {runId}-057` menampilkan Measurement `Box`

### TC-AC-DN-133: Edit nama Device Name yang punya SKU tanpa mengubah Category

28. Buka menu aksi pada baris `RFID Reader {runId}-057`, klik `Edit`
29. Kosongkan field Device Name lalu ketik "RFID Reader Pro {runId}-057"
30. Klik `[Save]`
31. Verifikasi toast sukses "Success, device name has been updated."
32. Verifikasi baris `RFID Reader Pro {runId}-057` tampil di List
33. Verifikasi kolom Brand baris `RFID Reader Pro {runId}-057` menampilkan chip `Brand A`, `Brand B`, dan `+1 more`
34. Verifikasi kolom Model/Type baris `RFID Reader Pro {runId}-057` menampilkan chip `Model R1`, `Model R2`, dan `+1 more`
35. Verifikasi baris `RFID Reader Pro {runId}-057` menampilkan Category badge `UHF Handheld`
36. Verifikasi baris `RFID Reader Pro {runId}-057` menampilkan Measurement `Unit`

### TC-AC-DN-588: Ubah Measurement pada Device Name yang punya SKU tanpa konfirmasi tambahan

37. Buka menu aksi pada baris `RFID Scanner {runId}-057`, klik `Edit`
38. Klik field Measurement lalu pilih `Box`
39. Klik `[Save]`
40. Verifikasi toast sukses "Success, device name has been updated."
41. Verifikasi popup form tertutup
42. Verifikasi tidak ada dialog konfirmasi tambahan
43. Verifikasi baris `RFID Scanner {runId}-057` menampilkan Measurement `Box`
44. Verifikasi baris `RFID Scanner {runId}-057` menampilkan Category badge `UHF Handheld` (tidak berubah)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (Search `{runId}-057`) menemukan baris record milik spec dan tidak memuat asersi. Search dianggap tetap aktif sesudah popup Edit disimpan atau ditutup; spec tidak mengulang Search per blok.
- Record milik spec (S-06, S-12): R1 sampai R4 menggantikan `Door Antenna` dan `RFID Reader` Pre-setup #16; R2 dan R3 membawa tiga SKU seperti `RFID Reader`; R3 dipakai TC-AC-DN-158 lalu TC-AC-DN-588 (TC-AC-DN-158 tidak mengubah record). Record Pre-setup #16 tidak diubah, sehingga nilai literal Last Modified Pre-setup #19 tidak dipakai dan Last Modified dibandingkan dengan nilai yang dicatat spec.
- Kategori uji (S-06, S-13): precondition TC-AC-DN-157 menambah Subcategory di bawah `Antenna` Pre-setup #14. Spec memakai node `Antena Uji {runId}-057` milik spec supaya pohon bersama tidak berubah; teks Category pada asersi memakai nama node itu, bukan `Antenna`.
- Penyimpangan urutan (S-10): blok diblokir (TC-AC-DN-158) dan no-op (TC-AC-DN-157) ditaruh sebelum blok yang menyimpan (TC-AC-DN-132, TC-AC-DN-133, TC-AC-DN-588) mengikuti urutan screening, validasi diblokir, lalu aksi sukses; tiap blok memakai record sendiri sehingga urutan tidak mengubah hasil.
- Langkah penghubung (S-03, S-08): langkah 8 sampai 10 menutup form dirty TC-AC-DN-158 secara deterministik (`[✕]`, dialog `Unsaved Changes`, `[Leave]`).
- Ukuran spec (44 langkah, di atas smell 35 langkah, kode R3): satu topik (Edit), satu halaman, satu kelas harness; lima blok TC memakai record sendiri (dua di antaranya dengan SKU) sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-132 (satu entri log Edit per field di tiga surface log), TC-AC-DN-133 (relasi SKU tidak berubah), TC-AC-DN-157 (tidak ada entri log baru, Category tersimpan tidak berubah), TC-AC-DN-158 (tidak ada entri log baru, ketiga SKU tetap ada), TC-AC-DN-588.
  - TC-AC-DN-132 hingga TC-AC-DN-588: TC sumber menyebut nama record Pre-setup #16 dan teks tanpa suffix; spec memakai nama bersuffix `{runId}-<NNN>` (S-12) pada seed, input, dan asersi, dan mengikuti teks UI TC persis.
