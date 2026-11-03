---
id: TC-AC-DN-E2E-066-edit-tutup-form-bersih
title: "Edit Device Name: Menutup Form Edit yang Belum Diubah (Icon Close, Esc, Backdrop)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-169
  - TC-AC-DN-170
  - TC-AC-DN-176
coverage:
  web: automated
---

# Edit Device Name: Menutup Form Edit yang Belum Diubah (Icon Close, Esc, Backdrop)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap yang dirujuk spec: email akun Pre-setup #1, Measurement master `Unit`, `Meter`, `Box`, serta nama node pohon Category. Nama record dinamis dibentuk `<nama dasar> {runId}-066` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja, tidak diubah): #13 Measurement `Unit`, `Meter`, `Box`; #14 Pohon Category (`Hardware` > `Smart Fixed Reader` > `Antenna`; `Hardware` > `Handheld Reader` > `UHF Handheld`; `TAG` > `NFC` > `Accessory`, `Tag`); #20 General Settings (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Record inti Pre-setup #16 tidak menjadi target aksi; target aksi memakai record milik spec di bawah (S-06).
- Data Dinamis (milik spec; dibuat lewat API di hook `before`, dihapus di hook `after` termasuk hasil rename; kemampuan seeding Device Name disediakan tim FE/BE). Last Modified record seed berisi waktu pembuatan karena belum ada entri Changelog.

  | Kode | Nama awal | Measurement | Category | SKU | Dipakai oleh |
  |---|---|---|---|---|---|
  | R1 | `Door Antenna {runId}-066` | `Unit` | `Antenna` | tanpa SKU | TC-AC-DN-169, TC-AC-DN-170, TC-AC-DN-176 |

- Tidak ada perubahan field dan tidak ada Save; popup dibuka tiga kali dan ditutup tiga kali.
- Kemampuan teknis: mengetik, menempel, memilih opsi dropdown dan node pohon Category, menekan Esc dan Tab, serta klik area gelap di luar popup.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Search `{runId}-066` yang aktif sepanjang spec dipulihkan (dikosongkan) bila langkah berikutnya bergantung pada daftar penuh.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Ketik Search `{runId}-066`, tekan Enter

### TC-AC-DN-169: Icon close pada form yang belum diubah

2. Buka menu aksi pada baris `Door Antenna {runId}-066`, klik `Edit`
3. Klik icon close `[✕]` pada popup
4. Verifikasi popup form tertutup langsung
5. Verifikasi dialog `Unsaved Changes` tidak muncul

### TC-AC-DN-170: Esc pada form yang belum diubah

6. Buka menu aksi pada baris `Door Antenna {runId}-066`, klik `Edit`
7. Tekan tombol `Esc`
8. Verifikasi popup form tertutup langsung
9. Verifikasi dialog `Unsaved Changes` tidak muncul

### TC-AC-DN-176: Klik backdrop pada form yang belum diubah

10. Buka menu aksi pada baris `Door Antenna {runId}-066`, klik `Edit`
11. Klik area gelap di luar popup
12. Verifikasi popup form Edit tetap terbuka
13. Verifikasi dialog `Unsaved Changes` tidak muncul
14. Klik icon close `[✕]` pada popup

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (Search `{runId}-066`) menemukan baris record milik spec dan tidak memuat asersi. Search dianggap tetap aktif sesudah popup Edit disimpan atau ditutup; spec tidak mengulang Search per blok.
- Record milik spec (S-06, S-12): R1 menggantikan `Door Antenna` Pre-setup #16 dan tidak pernah diubah. Record Pre-setup #16 tidak diubah, sehingga nilai literal Last Modified Pre-setup #19 tidak dipakai dan Last Modified dibandingkan dengan nilai yang dicatat spec.
- Urutan: TC-AC-DN-176 (popup tetap terbuka) di akhir; langkah 14 menutup popup yang masih terbuka dan form bersih sehingga ditutup langsung tanpa dialog (penghubung, S-03). Tiga kali buka sama dengan tiga kali tutup.
- Temuan untuk QA:
  - TC-AC-DN-169, TC-AC-DN-170, dan TC-AC-DN-176 tidak punya Post Condition.
  - TC-AC-DN-169 hingga TC-AC-DN-176: TC sumber menyebut nama record Pre-setup #16 dan teks tanpa suffix; spec memakai nama bersuffix `{runId}-<NNN>` (S-12) pada seed, input, dan asersi, dan mengikuti teks UI TC persis.
