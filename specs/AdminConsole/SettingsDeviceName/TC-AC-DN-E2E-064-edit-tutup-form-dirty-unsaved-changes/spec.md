---
id: TC-AC-DN-E2E-064-edit-tutup-form-dirty-unsaved-changes
title: "Edit Device Name: Menutup Form Dirty dan Dialog Unsaved Changes"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-171
  - TC-AC-DN-172
  - TC-AC-DN-173
  - TC-AC-DN-174
coverage:
  web: automated
---

# Edit Device Name: Menutup Form Dirty dan Dialog Unsaved Changes

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap yang dirujuk spec: email akun Pre-setup #1, Measurement master `Unit`, `Meter`, `Box`, serta nama node pohon Category. Nama record dinamis dibentuk `<nama dasar> {runId}-064` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja, tidak diubah): #13 Measurement `Unit`, `Meter`, `Box`; #14 Pohon Category (`Hardware` > `Smart Fixed Reader` > `Antenna`; `Hardware` > `Handheld Reader` > `UHF Handheld`; `TAG` > `NFC` > `Accessory`, `Tag`); #20 General Settings (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Record inti Pre-setup #16 tidak menjadi target aksi; target aksi memakai record milik spec di bawah (S-06).
- Data Dinamis (milik spec; dibuat lewat API di hook `before`, dihapus di hook `after` termasuk hasil rename; kemampuan seeding Device Name disediakan tim FE/BE). Last Modified record seed berisi waktu pembuatan karena belum ada entri Changelog.

  | Kode | Nama awal | Measurement | Category | SKU | Dipakai oleh |
  |---|---|---|---|---|---|
  | R1 | `Door Antenna {runId}-064` | `Unit` | `Antenna` | tanpa SKU | TC-AC-DN-171 sampai TC-AC-DN-174 |

- Satu popup Edit R1 dibuka sekali dan dipakai berulang; isian "Door Draft" dan Measurement `Meter` tidak pernah disimpan, dan popup ditutup lewat `[Leave]` di akhir.
- Kemampuan teknis: mengetik, menempel, memilih opsi dropdown dan node pohon Category, menekan Esc dan Tab, serta klik area gelap di luar popup.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Search `{runId}-064` yang aktif sepanjang spec dipulihkan (dikosongkan) bila langkah berikutnya bergantung pada daftar penuh.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Ketik Search `{runId}-064`, tekan Enter
2. Buka menu aksi pada baris `Door Antenna {runId}-064`, klik `Edit`

### TC-AC-DN-171: Menutup form Edit yang sudah diubah lewat icon close

3. Kosongkan field Device Name lalu ketik "Door Draft"
4. Klik icon close `[✕]` pada popup
5. Verifikasi dialog `Unsaved Changes` tampil dengan Body "You have unsaved changes. Are you sure you want to leave?"
6. Verifikasi dialog memuat tombol `[Cancel]` dan `[Leave]`
7. Verifikasi popup form Edit tetap terbuka di belakang dialog
8. Verifikasi isian `Door Draft` dipertahankan

### TC-AC-DN-173: Tombol Cancel pada dialog Unsaved Changes

9. Klik `[Cancel]` pada dialog
10. Verifikasi dialog tertutup
11. Verifikasi popup form Edit tetap terbuka dengan Device Name `Door Draft` dipertahankan

### TC-AC-DN-172: Menutup form Edit dengan Esc setelah mengubah Measurement

12. Klik field Measurement lalu pilih `Meter`
13. Tekan tombol `Esc`
14. Verifikasi dialog `Unsaved Changes` tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" serta tombol `[Cancel]` dan `[Leave]`

### TC-AC-DN-174: Tombol Leave menutup form tanpa menyimpan

15. Klik `[Cancel]` pada dialog
16. Klik icon close `[✕]` pada popup
17. Verifikasi dialog `Unsaved Changes` tampil
18. Klik `[Leave]` pada dialog
19. Verifikasi dialog dan popup form Edit tertutup
20. Verifikasi List tetap memuat baris `Door Antenna {runId}-064`
21. Verifikasi List tidak memuat `Door Draft`
22. Verifikasi tidak ada toast

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (Search `{runId}-064`) menemukan baris record milik spec dan tidak memuat asersi. Search dianggap tetap aktif sesudah popup Edit disimpan atau ditutup; spec tidak mengulang Search per blok.
- Record milik spec (S-06, S-12): R1 menggantikan `Door Antenna` Pre-setup #16 dan tidak pernah tersimpan berubah. Record Pre-setup #16 tidak diubah, sehingga nilai literal Last Modified Pre-setup #19 tidak dipakai dan Last Modified dibandingkan dengan nilai yang dicatat spec.
- Satu pembukaan popup dipakai berulang (prinsip 13): TC-AC-DN-171, TC-AC-DN-173, TC-AC-DN-172, dan TC-AC-DN-174 saling melanjutkan state form dirty yang sama (isian "Door Draft"). TC-AC-DN-173 ditaruh sebelum TC-AC-DN-172 karena memakai dialog dari langkah 4; TC-AC-DN-172 menambah perubahan Measurement `Meter` sehingga form pada TC-AC-DN-174 berisi "Door Draft" dan `Meter`.
- Langkah penghubung (S-03): langkah 15 (`[Cancel]`) mengembalikan form dari dialog yang dibuka Esc sebelum TC-AC-DN-174 menutupnya lewat `[✕]`.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-174 (record `Door Antenna` tidak berubah).
  - TC-AC-DN-171 hingga TC-AC-DN-174: TC sumber menyebut nama record Pre-setup #16 dan teks tanpa suffix; spec memakai nama bersuffix `{runId}-<NNN>` (S-12) pada seed, input, dan asersi, dan mengikuti teks UI TC persis.
