---
id: TC-AC-DN-E2E-061-edit-emoji-dan-simbol
title: "Edit Device Name: Emoji Diketik, Ditempel, Lolos Filter FE, dan Simbol Umum"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-148
  - TC-AC-DN-149
  - TC-AC-DN-150
  - TC-AC-DN-151
coverage:
  web: automated
---

# Edit Device Name: Emoji Diketik, Ditempel, Lolos Filter FE, dan Simbol Umum

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap yang dirujuk spec: email akun Pre-setup #1, Measurement master `Unit`, `Meter`, `Box`, serta nama node pohon Category. Nama record dinamis dibentuk `<nama dasar> {runId}-061` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja, tidak diubah): #13 Measurement `Unit`, `Meter`, `Box`; #14 Pohon Category (`Hardware` > `Smart Fixed Reader` > `Antenna`; `Hardware` > `Handheld Reader` > `UHF Handheld`; `TAG` > `NFC` > `Accessory`, `Tag`); #20 General Settings (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Record inti Pre-setup #16 tidak menjadi target aksi; target aksi memakai record milik spec di bawah (S-06).
- Data Dinamis (milik spec; dibuat lewat API di hook `before`, dihapus di hook `after` termasuk hasil rename; kemampuan seeding Device Name disediakan tim FE/BE). Last Modified record seed berisi waktu pembuatan karena belum ada entri Changelog.

  | Kode | Nama awal | Measurement | Category | SKU | Dipakai oleh |
  |---|---|---|---|---|---|
  | R1 | `Door Antenna {runId}-061` | `Unit` | `Antenna` | tanpa SKU | TC-AC-DN-148, TC-AC-DN-149, TC-AC-DN-150, TC-AC-DN-151 |

- Satu popup Edit R1 dipakai berulang untuk keempat TC; hanya TC-AC-DN-151 yang menyimpan, sehingga popup tertutup oleh Save di akhir.
- Kemampuan teknis: mengetik lewat keyboard, menyalin teks ke clipboard dan menempelnya ke field, serta menyisipkan karakter langsung ke nilai input lewat console browser (melewati filter keystroke dan paste).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Search `{runId}-061` yang aktif sepanjang spec dipulihkan (dikosongkan) bila langkah berikutnya bergantung pada daftar penuh.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Ketik Search `{runId}-061`, tekan Enter
2. Buka menu aksi pada baris `Door Antenna {runId}-061`, klik `Edit`

### TC-AC-DN-148: Emoji yang diketik diblok

3. Klik di akhir isi field Device Name lalu ketik "😊" dengan keyboard
4. Verifikasi field Device Name tetap berisi `Door Antenna {runId}-061`; karakter emoji tidak masuk ke field
5. Verifikasi tidak ada pesan error

### TC-AC-DN-149: Emoji yang ditempel diblok

6. Salin teks "Pintu🔥Utama" ke clipboard
7. Kosongkan field Device Name lalu tempel (paste) ke field
8. Verifikasi field Device Name hanya berisi `PintuUtama`; karakter emoji tidak masuk ke field
9. Verifikasi tidak ada pesan error

### TC-AC-DN-150: Emoji yang lolos filter FE ditolak saat Save

10. Kosongkan field Device Name lalu ketik "Door Antenna {runId}-061"
11. Lewat console browser, sisipkan karakter 😊 langsung ke nilai input Device Name sehingga melewati filter keystroke dan paste
12. Klik `[Save]`
13. Verifikasi error inline "Device name contains invalid characters" muncul di bawah field Device Name
14. Verifikasi popup form tetap terbuka
15. Verifikasi tidak ada toast sukses

### TC-AC-DN-151: Tanda baca dan simbol umum diterima

16. Kosongkan field Device Name lalu ketik "Pintu (Utama) - #2 & Co. 50% @Lobi {runId}-061"
17. Verifikasi tidak ada pesan error karakter
18. Klik `[Save]`
19. Verifikasi toast sukses "Success, device name has been updated."
20. Verifikasi List memuat baris `Pintu (Utama) - #2 & Co. 50% @Lobi {runId}-061`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (Search `{runId}-061`) menemukan baris record milik spec dan tidak memuat asersi. Search dianggap tetap aktif sesudah popup Edit disimpan atau ditutup; spec tidak mengulang Search per blok.
- Record milik spec (S-06, S-12): R1 menggantikan `Door Antenna` Pre-setup #16; hanya TC-AC-DN-151 yang menyimpannya. Record Pre-setup #16 tidak diubah, sehingga nilai literal Last Modified Pre-setup #19 tidak dipakai dan Last Modified dibandingkan dengan nilai yang dicatat spec.
- Satu pembukaan popup dipakai berulang (prinsip 13): TC-AC-DN-148 sampai TC-AC-DN-150 hanya mengetik atau menempel; langkah 10 mengembalikan isi field ke nilai awal sebelum TC-AC-DN-150 (penghubung, S-03).
- Urutan: mengikuti sourceTc (TC-AC-DN-151 yang menyimpan di akhir).
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-150 (record `Door Antenna` tidak berubah), TC-AC-DN-151 (nama tersimpan sama persis dengan input).
  - TC-AC-DN-148 hingga TC-AC-DN-151: TC sumber menyebut nama record Pre-setup #16 dan teks tanpa suffix; spec memakai nama bersuffix `{runId}-<NNN>` (S-12) pada seed, input, dan asersi, dan mengikuti teks UI TC persis.
  - TC-AC-DN-150 tidak menjelaskan cara menyisipkan karakter lewat console; spec menulisnya sebagai kemampuan teknis tanpa mengarang mekanisme lain.
