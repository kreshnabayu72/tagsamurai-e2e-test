---
id: TC-AC-DN-E2E-062-edit-validasi-duplikat
title: "Edit Device Name: Duplikat (Persis, Huruf Besar-Kecil, Spasi Ujung) dan Nama Sendiri Bukan Duplikat"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-143
  - TC-AC-DN-144
  - TC-AC-DN-145
  - TC-AC-DN-146
coverage:
  web: automated
---

# Edit Device Name: Duplikat (Persis, Huruf Besar-Kecil, Spasi Ujung) dan Nama Sendiri Bukan Duplikat

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap yang dirujuk spec: email akun Pre-setup #1, Measurement master `Unit`, `Meter`, `Box`, serta nama node pohon Category. Nama record dinamis dibentuk `<nama dasar> {runId}-062` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja, tidak diubah): #13 Measurement `Unit`, `Meter`, `Box`; #14 Pohon Category (`Hardware` > `Smart Fixed Reader` > `Antenna`; `Hardware` > `Handheld Reader` > `UHF Handheld`; `TAG` > `NFC` > `Accessory`, `Tag`); #20 General Settings (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Record inti Pre-setup #16 tidak menjadi target aksi; target aksi memakai record milik spec di bawah (S-06).
- Data Dinamis (milik spec; dibuat lewat API di hook `before`, dihapus di hook `after` termasuk hasil rename; kemampuan seeding Device Name disediakan tim FE/BE). Last Modified record seed berisi waktu pembuatan karena belum ada entri Changelog.

  | Kode | Nama awal | Measurement | Category | SKU | Dipakai oleh |
  |---|---|---|---|---|---|
  | R1 | `Door Antenna {runId}-062` | `Unit` | `Antenna` | tanpa SKU | TC-AC-DN-143 sampai TC-AC-DN-146 (record yang diedit) |
  | R2 | `Cable Tester {runId}-062` | `Unit` | `Accessory` | tanpa SKU | TC-AC-DN-143, TC-AC-DN-145 (nama pembanding duplikat) |
  | R3 | `Gate Antenna {runId}-062` | `Unit` | `Antenna` | tanpa SKU | TC-AC-DN-144 (nama pembanding huruf besar-kecil) |

- Satu popup Edit R1 dipakai berulang; tidak ada Save yang berhasil. Pemeriksaan duplikat berjalan setelah jeda sekitar 500 ms tanpa memindahkan fokus (jeda pendek, disebut TC).
- Kemampuan teknis: mengetik, menempel, memilih opsi dropdown dan node pohon Category, menekan Esc dan Tab, serta klik area gelap di luar popup.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Search `{runId}-062` yang aktif sepanjang spec dipulihkan (dikosongkan) bila langkah berikutnya bergantung pada daftar penuh.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Ketik Search `{runId}-062`, tekan Enter
2. Buka menu aksi pada baris `Door Antenna {runId}-062`, klik `Edit`

### TC-AC-DN-143: Nama sama persis dengan record lain

3. Kosongkan field Device Name lalu ketik "Cable Tester {runId}-062"
4. Tunggu sekitar 500 ms tanpa memindahkan fokus
5. Verifikasi error inline "Device name already exists" muncul di bawah field Device Name setelah jeda sekitar 500 ms, tanpa klik di luar field
6. Klik `[Save]`
7. Verifikasi error inline "Device name already exists" tetap tampil
8. Verifikasi popup form tetap terbuka
9. Verifikasi tidak ada toast

### TC-AC-DN-144: Nama hanya berbeda huruf besar-kecil

10. Kosongkan field Device Name lalu ketik "Door Antenna {runId}-062"
11. Kosongkan field Device Name lalu ketik "gate antenna {runId}-062"
12. Tunggu sekitar 500 ms tanpa memindahkan fokus
13. Verifikasi error inline "Device name already exists" muncul di bawah field Device Name
14. Verifikasi popup form tetap terbuka

### TC-AC-DN-145: Nama duplikat disertai spasi di ujung

15. Kosongkan field Device Name lalu ketik "Door Antenna {runId}-062"
16. Kosongkan field Device Name lalu ketik "  Cable Tester {runId}-062  " (dua spasi di awal dan di akhir)
17. Tunggu sekitar 500 ms tanpa memindahkan fokus
18. Verifikasi error inline "Device name already exists" muncul di bawah field Device Name karena pengecekan memakai nilai ter-trim

### TC-AC-DN-146: Mengetik kembali nama milik record yang sedang diedit

19. Kosongkan field Device Name lalu ketik "Door Antenna Baru {runId}-062"
20. Kosongkan field Device Name lalu ketik kembali "Door Antenna {runId}-062"
21. Tunggu sekitar 500 ms tanpa memindahkan fokus
22. Verifikasi field Device Name berisi `Door Antenna {runId}-062`
23. Verifikasi tidak ada error `Device name already exists`
24. Klik icon close `[✕]` pada popup

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (Search `{runId}-062`) menemukan baris record milik spec dan tidak memuat asersi. Search dianggap tetap aktif sesudah popup Edit disimpan atau ditutup; spec tidak mengulang Search per blok.
- Record milik spec (S-06, S-12): R1 menggantikan `Door Antenna`; R2 dan R3 menggantikan record pembanding `Cable Tester` dan `Gate Antenna` Pre-setup #16 yang dibuat milik spec agar Pre-setup tidak dipakai sebagai pembanding bersama. Record Pre-setup #16 tidak diubah, sehingga nilai literal Last Modified Pre-setup #19 tidak dipakai dan Last Modified dibandingkan dengan nilai yang dicatat spec.
- Satu pembukaan popup dipakai berulang (prinsip 13): TC-AC-DN-143 sampai TC-AC-DN-146 hanya mengetik dan menunggu; langkah 10, 15, dan 19 mengembalikan isi field ke nilai yang valid sebagai pembersih error inline identik antar-TC (R-12, penghubung S-03).
- Asersi tambahan (S-03): langkah 22 memverifikasi isi field sebagai anchor positif sebelum asersi absence error pada langkah 23 (bagian 8b butir 2); tidak ada di Expected TC-AC-DN-146.
- Penutupan form: sesudah TC-AC-DN-146 isi field kembali sama dengan nilai tersimpan (form bersih, TC-AC-DN-175), sehingga `[✕]` pada langkah 24 menutup popup tanpa dialog `Unsaved Changes`.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-143 dan TC-AC-DN-144 (record `Door Antenna` tidak berubah). TC-AC-DN-145 tidak punya Post Condition.
  - TC-AC-DN-143 hingga TC-AC-DN-146: TC sumber menyebut nama record Pre-setup #16 dan teks tanpa suffix; spec memakai nama bersuffix `{runId}-<NNN>` (S-12) pada seed, input, dan asersi, dan mengikuti teks UI TC persis.
