---
id: TC-AC-DN-E2E-056-edit-screening-dan-ubah-satu-field
title: "Edit Device Name: Screening Popup dan Ubah Nama, Measurement, Category, serta Rename Memindahkan Baris"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-128
  - TC-AC-DN-129
  - TC-AC-DN-130
  - TC-AC-DN-131
  - TC-AC-DN-587
coverage:
  web: automated
---

# Edit Device Name: Screening Popup dan Ubah Nama, Measurement, Category, serta Rename Memindahkan Baris

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap yang dirujuk spec: email akun Pre-setup #1, Measurement master `Unit`, `Meter`, `Box`, serta nama node pohon Category. Nama record dinamis dibentuk `<nama dasar> {runId}-056` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja, tidak diubah): #13 Measurement `Unit`, `Meter`, `Box`; #14 Pohon Category (`Hardware` > `Smart Fixed Reader` > `Antenna`; `Hardware` > `Handheld Reader` > `UHF Handheld`; `TAG` > `NFC` > `Accessory`, `Tag`); #20 General Settings (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Record inti Pre-setup #16 tidak menjadi target aksi; target aksi memakai record milik spec di bawah (S-06).
- Data Dinamis (milik spec; dibuat lewat API di hook `before`, dihapus di hook `after` termasuk hasil rename; kemampuan seeding Device Name disediakan tim FE/BE). Last Modified record seed berisi waktu pembuatan karena belum ada entri Changelog.

  | Kode | Nama awal | Measurement | Category | SKU | Dipakai oleh |
  |---|---|---|---|---|---|
  | R1 | `Door Antenna {runId}-056` | `Unit` | `Antenna` | tanpa SKU | TC-AC-DN-128, TC-AC-DN-129 |
  | R2 | `Door Meter {runId}-056` | `Unit` | `Antenna` | tanpa SKU | TC-AC-DN-130 |
  | R3 | `Door Kategori {runId}-056` | `Unit` | `Antenna` | tanpa SKU | TC-AC-DN-131 |
  | R4 | `Door Alfabet {runId}-056` | `Unit` | `Antenna` | tanpa SKU | TC-AC-DN-587 |

- Asersi Last Modified (TC-AC-DN-129): waktu dicatat sesudah klik `[Save]`, Last Modified dibandingkan dengan waktu itu dengan toleransi satu menit; jam server dan jam browser sinkron.
- Kemampuan teknis: mengetik, menempel, memilih opsi dropdown dan node pohon Category, menekan Esc dan Tab, serta klik area gelap di luar popup.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Search `{runId}-056` yang aktif sepanjang spec dipulihkan (dikosongkan) bila langkah berikutnya bergantung pada daftar penuh.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Ketik Search `{runId}-056`, tekan Enter

### TC-AC-DN-128: Screening popup form Edit Device Name

2. Buka menu aksi pada baris `Door Antenna {runId}-056`, klik `Edit`
3. Verifikasi judul popup `Edit Device Name` tampil di sisi kiri atas header
4. Verifikasi icon close `[✕]` tampil di sudut kanan atas popup
5. Verifikasi field Device Name berisi `Door Antenna {runId}-056`
6. Verifikasi field Measurement menampilkan `Unit`
7. Verifikasi field Category menampilkan `Antenna`
8. Verifikasi tidak ada pesan error pada field
9. Verifikasi tombol `[Clear Field]` (teks, primary) dan `[Save]` (filled, success) berdampingan rata kanan di footer
10. Verifikasi checkbox `Stay on this form after submitting` tidak tampil
11. Verifikasi tidak ada tombol `[Cancel]`

### TC-AC-DN-129: Edit mengubah Device Name saja

12. Kosongkan field Device Name lalu ketik "Door Antenna Pro {runId}-056"
13. Klik `[Save]`, lalu catat waktu sesudah Save
14. Verifikasi toast sukses "Success, device name has been updated."
15. Verifikasi popup form tertutup
16. Verifikasi baris `Door Antenna Pro {runId}-056` tampil di List
17. Verifikasi baris `Door Antenna Pro {runId}-056` menampilkan Category `Antenna`
18. Verifikasi baris `Door Antenna Pro {runId}-056` menampilkan Measurement `Unit`
19. Verifikasi baris `Door Antenna {runId}-056` tidak lagi tampil di List
20. Verifikasi kolom Last Modified baris `Door Antenna Pro {runId}-056` menampilkan waktu Save yang dicatat, format `dd/MM/yy HH:mm` Asia/Jakarta

### TC-AC-DN-130: Edit mengubah Measurement saja

21. Buka menu aksi pada baris `Door Meter {runId}-056`, klik `Edit`
22. Klik field Measurement lalu pilih `Meter`
23. Klik `[Save]`
24. Verifikasi toast sukses "Success, device name has been updated."
25. Verifikasi baris `Door Meter {runId}-056` menampilkan Measurement `Meter`
26. Verifikasi baris `Door Meter {runId}-056` menampilkan Category `Antenna` (tidak berubah)

### TC-AC-DN-131: Edit mengubah Category saja pada Device Name tanpa SKU

27. Buka menu aksi pada baris `Door Kategori {runId}-056`, klik `Edit`
28. Klik field Category, expand `TAG` lalu `NFC`, pilih leaf `Accessory`
29. Klik `[Save]`
30. Verifikasi toast sukses "Success, device name has been updated."
31. Verifikasi baris `Door Kategori {runId}-056` menampilkan Category badge `Accessory`
32. Verifikasi baris `Door Kategori {runId}-056` menampilkan Measurement `Unit` (tidak berubah)

### TC-AC-DN-587: Rename memindahkan baris ke posisi alfabetis baru

33. Buka menu aksi pada baris `Door Alfabet {runId}-056`, klik `Edit`
34. Kosongkan field Device Name lalu ketik "Alpha Antenna {runId}-056"
35. Klik `[Save]`
36. Verifikasi toast sukses "Success, device name has been updated."
37. Verifikasi popup form tertutup
38. Verifikasi baris `Door Alfabet {runId}-056` tidak lagi tampil di List
39. Klik `(←)` pada kotak Search
40. Verifikasi baris pertama List adalah `Alpha Antenna {runId}-056` (urutan A-Z, sebelum `Barcode Station`)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (Search `{runId}-056`) menemukan baris record milik spec dan tidak memuat asersi. Search dianggap tetap aktif sesudah popup Edit disimpan atau ditutup; spec tidak mengulang Search per blok.
- Record milik spec (S-06, S-12): R1 sampai R4 dibuat satu per blok TC supaya tiap blok memakai kondisi awal TC (Measurement `Unit`, Category `Antenna`); TC sumber memakai satu `Door Antenna` yang dipulihkan antar TC. Record Pre-setup #16 tidak diubah, sehingga nilai literal Last Modified Pre-setup #19 tidak dipakai dan Last Modified dibandingkan dengan nilai yang dicatat spec.
- Urutan: mengikuti sourceTc; blok rename yang memindahkan baris (TC-AC-DN-587) di akhir karena Search dikosongkan di langkah 39 untuk menilai posisi baris pertama.
- Ukuran spec (40 langkah, di atas smell 35 langkah, kode R3): satu topik (Edit satu field), satu halaman, satu kelas harness, empat record terpisah sehingga tiap blok TC berdiri sendiri dan bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-129 (entri log Edit di tiga surface log dan nama baru pada dropdown Device SKU), TC-AC-DN-130, TC-AC-DN-131, TC-AC-DN-587.
  - TC-AC-DN-128 hingga TC-AC-DN-587: TC sumber menyebut nama record Pre-setup #16 dan teks tanpa suffix; spec memakai nama bersuffix `{runId}-<NNN>` (S-12) pada seed, input, dan asersi, dan mengikuti teks UI TC persis.
  - TC-AC-DN-587 mensyaratkan baris pertama List berurutan A-Z; spec mengasumsikan tidak ada record lain yang berurutan sebelum `Alpha Antenna`.
