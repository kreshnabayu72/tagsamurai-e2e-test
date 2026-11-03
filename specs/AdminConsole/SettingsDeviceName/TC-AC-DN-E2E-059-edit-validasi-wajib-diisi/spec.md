---
id: TC-AC-DN-E2E-059-edit-validasi-wajib-diisi
title: "Edit Device Name: Validasi Wajib Diisi dan Klik Root Hardware/TAG"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-137
  - TC-AC-DN-138
  - TC-AC-DN-152
  - TC-AC-DN-153
  - TC-AC-DN-154
coverage:
  web: automated
---

# Edit Device Name: Validasi Wajib Diisi dan Klik Root Hardware/TAG

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap yang dirujuk spec: email akun Pre-setup #1, Measurement master `Unit`, `Meter`, `Box`, serta nama node pohon Category. Nama record dinamis dibentuk `<nama dasar> {runId}-059` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja, tidak diubah): #13 Measurement `Unit`, `Meter`, `Box`; #14 Pohon Category (`Hardware` > `Smart Fixed Reader` > `Antenna`; `Hardware` > `Handheld Reader` > `UHF Handheld`; `TAG` > `NFC` > `Accessory`, `Tag`); #20 General Settings (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Record inti Pre-setup #16 tidak menjadi target aksi; target aksi memakai record milik spec di bawah (S-06).
- Data Dinamis (milik spec; dibuat lewat API di hook `before`, dihapus di hook `after` termasuk hasil rename; kemampuan seeding Device Name disediakan tim FE/BE). Last Modified record seed berisi waktu pembuatan karena belum ada entri Changelog.

  | Kode | Nama awal | Measurement | Category | SKU | Dipakai oleh |
  |---|---|---|---|---|---|
  | R1 | `Door Antenna {runId}-059` | `Unit` | `Antenna` | tanpa SKU | TC-AC-DN-137, TC-AC-DN-138, TC-AC-DN-152, TC-AC-DN-153, TC-AC-DN-154 |

- Satu popup Edit R1 dibuka sekali dan dipakai berulang untuk kelima TC (semua kasus diblokir validasi, record tidak pernah tersimpan); popup ditutup di akhir spec.
- Kemampuan teknis: mengetik, menempel, memilih opsi dropdown dan node pohon Category, menekan Esc dan Tab, serta klik area gelap di luar popup.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Search `{runId}-059` yang aktif sepanjang spec dipulihkan (dikosongkan) bila langkah berikutnya bergantung pada daftar penuh.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Ketik Search `{runId}-059`, tekan Enter
2. Buka menu aksi pada baris `Door Antenna {runId}-059`, klik `Edit`

### TC-AC-DN-154: Klik root Hardware dan TAG pada dropdown Category

3. Klik field Category
4. Klik node `Hardware`
5. Klik node `TAG`
6. Verifikasi field Category tetap menampilkan `Antenna` (pilihan tersimpan)
7. Verifikasi `Hardware` dan `TAG` tidak berstatus terpilih

### TC-AC-DN-137: Save Edit dengan Device Name kosong

8. Klik judul popup `Edit Device Name` untuk menutup pohon Category
9. Klik `[Clear Field]`
10. Klik field Measurement lalu pilih `Unit`
11. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
12. Klik `[Save]`
13. Verifikasi error inline di bawah field Device Name "Device name must not be empty"
14. Verifikasi popup form tetap terbuka
15. Verifikasi field Measurement tetap menampilkan `Unit`
16. Verifikasi field Category tetap menampilkan `Antenna`
17. Verifikasi tidak ada toast

### TC-AC-DN-138: Save Edit dengan Device Name hanya spasi

18. Ketik "Tmp" pada field Device Name
19. Kosongkan field Device Name lalu ketik lima spasi
20. Klik `[Save]`
21. Verifikasi error inline di bawah field Device Name "Device name must not be empty"
22. Verifikasi popup form tetap terbuka

### TC-AC-DN-152: Save Edit tanpa Measurement

23. Klik `[Clear Field]`
24. Ketik "Door Antenna {runId}-059" pada field Device Name
25. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
26. Klik `[Save]`
27. Verifikasi error inline di bawah field Measurement "Measurement must not be empty"
28. Verifikasi popup form tetap terbuka
29. Verifikasi field Device Name tetap berisi `Door Antenna {runId}-059`
30. Verifikasi field Category tetap menampilkan `Antenna`

### TC-AC-DN-153: Save Edit tanpa Category

31. Klik `[Clear Field]`
32. Ketik "Door Antenna {runId}-059" pada field Device Name
33. Klik field Measurement lalu pilih `Unit`
34. Klik `[Save]`
35. Verifikasi error inline di bawah field Category "Category must not be empty"
36. Verifikasi popup form tetap terbuka
37. Verifikasi field Device Name tetap berisi `Door Antenna {runId}-059`
38. Verifikasi field Measurement tetap menampilkan `Unit`
39. Klik icon close `[✕]` pada popup
40. Verifikasi dialog `Unsaved Changes` tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" serta tombol `[Cancel]` dan `[Leave]`
41. Klik `[Leave]` pada dialog

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (Search `{runId}-059`) menemukan baris record milik spec dan tidak memuat asersi. Search dianggap tetap aktif sesudah popup Edit disimpan atau ditutup; spec tidak mengulang Search per blok.
- Record milik spec (S-06, S-12): R1 menggantikan `Door Antenna` Pre-setup #16 dan tidak pernah tersimpan berubah. Record Pre-setup #16 tidak diubah, sehingga nilai literal Last Modified Pre-setup #19 tidak dipakai dan Last Modified dibandingkan dengan nilai yang dicatat spec.
- Satu pembukaan popup dipakai berulang (prinsip 13, "halaman yang sama dipakai berulang"): kelima TC hanya mengetik dan menekan `[Save]` yang diblokir validasi. TC-AC-DN-154 ditaruh pertama karena membutuhkan Category tersimpan `Antenna` yang belum diubah.
- Langkah penghubung (S-03, R-12): langkah 8 menutup pohon Category; langkah 18 membersihkan error inline sebelum kasus berikutnya berisi error yang sama (R-12); langkah 39 sampai 41 menutup form dirty secara deterministik (S-08).
- Ukuran spec (41 langkah, di atas smell 35 langkah, kode R1): halaman dan popup yang sama dipakai berulang; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01) dan tiap kasus mengatur ulang isian. Satu kelas harness, satu record, tanpa aksi tulis.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-137, TC-AC-DN-138, TC-AC-DN-152, TC-AC-DN-153 (record `Door Antenna` tidak berubah).
  - TC-AC-DN-137 hingga TC-AC-DN-154: TC sumber menyebut nama record Pre-setup #16 dan teks tanpa suffix; spec memakai nama bersuffix `{runId}-<NNN>` (S-12) pada seed, input, dan asersi, dan mengikuti teks UI TC persis.
