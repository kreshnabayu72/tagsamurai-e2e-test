---
id: TC-AC-DN-E2E-058-edit-no-op-kapitalisasi-spasi-dan-aksesibilitas
title: "Edit Device Name: Save Tanpa Perubahan, Hanya Huruf Besar-Kecil atau Spasi Ujung, dan Aksesibilitas Popup"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-134
  - TC-AC-DN-135
  - TC-AC-DN-136
  - TC-AC-DN-180
coverage:
  web: automated
---

# Edit Device Name: Save Tanpa Perubahan, Hanya Huruf Besar-Kecil atau Spasi Ujung, dan Aksesibilitas Popup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap yang dirujuk spec: email akun Pre-setup #1, Measurement master `Unit`, `Meter`, `Box`, serta nama node pohon Category. Nama record dinamis dibentuk `<nama dasar> {runId}-058` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja, tidak diubah): #13 Measurement `Unit`, `Meter`, `Box`; #14 Pohon Category (`Hardware` > `Smart Fixed Reader` > `Antenna`; `Hardware` > `Handheld Reader` > `UHF Handheld`; `TAG` > `NFC` > `Accessory`, `Tag`); #20 General Settings (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Record inti Pre-setup #16 tidak menjadi target aksi; target aksi memakai record milik spec di bawah (S-06).
- Data Dinamis (milik spec; dibuat lewat API di hook `before`, dihapus di hook `after` termasuk hasil rename; kemampuan seeding Device Name disediakan tim FE/BE). Last Modified record seed berisi waktu pembuatan karena belum ada entri Changelog.

  | Kode | Nama awal | Measurement | Category | SKU | Dipakai oleh |
  |---|---|---|---|---|---|
  | R1 | `Cable Tester {runId}-058` | `Unit` | `Accessory` | tanpa SKU | TC-AC-DN-134, TC-AC-DN-136 |
  | R2 | `RFID Reader {runId}-058` | `Unit` | `UHF Handheld` | tanpa SKU | TC-AC-DN-135 |
  | R3 | `Door Antenna {runId}-058` | `Unit` | `Antenna` | tanpa SKU | TC-AC-DN-180 |

- Nilai Last Modified R1 dan R2 dibaca dari List pada langkah 2 sebelum aksi dan menjadi pembanding asersi "tetap"; aksi no-op tidak mengubahnya.
- Kemampuan teknis: membaca atribut aksesibilitas (label, aria-required, aria-describedby) dan perilaku fokus Tab pada popup, serta mengetik, memilih opsi dropdown, dan menekan Tab.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Search `{runId}-058` yang aktif sepanjang spec dipulihkan (dikosongkan) bila langkah berikutnya bergantung pada daftar penuh.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Ketik Search `{runId}-058`, tekan Enter
2. Catat nilai kolom Last Modified baris `Cable Tester {runId}-058` dan baris `RFID Reader {runId}-058`

### TC-AC-DN-134: Save Edit tanpa mengubah nilai

3. Buka menu aksi pada baris `Cable Tester {runId}-058`, klik `Edit`
4. Klik `[Save]` tanpa mengubah isian
5. Verifikasi toast netral "No changes to save."
6. Verifikasi popup form tertutup
7. Verifikasi tidak ada error inline duplikat terhadap diri sendiri
8. Verifikasi kolom Last Modified baris `Cable Tester {runId}-058` sama dengan nilai yang dicatat pada langkah 2

### TC-AC-DN-135: Save Edit yang hanya mengubah huruf besar-kecil

9. Buka menu aksi pada baris `RFID Reader {runId}-058`, klik `Edit`
10. Kosongkan field Device Name lalu ketik "rfid reader {runId}-058"
11. Klik `[Save]`
12. Verifikasi toast netral "No changes to save."
13. Verifikasi popup form tertutup
14. Verifikasi baris tetap bernama `RFID Reader {runId}-058` (kapitalisasi tersimpan tidak berubah)
15. Verifikasi kolom Last Modified baris `RFID Reader {runId}-058` sama dengan nilai yang dicatat pada langkah 2

### TC-AC-DN-136: Save Edit yang hanya menambah spasi di ujung nama

16. Buka menu aksi pada baris `Cable Tester {runId}-058`, klik `Edit`
17. Ketik tiga spasi di akhir isi field Device Name
18. Klik `[Save]`
19. Verifikasi toast netral "No changes to save."
20. Verifikasi popup form tertutup
21. Verifikasi baris tetap bernama `Cable Tester {runId}-058`
22. Verifikasi kolom Last Modified baris `Cable Tester {runId}-058` sama dengan nilai yang dicatat pada langkah 2

### TC-AC-DN-180: Aksesibilitas popup Edit

23. Buka menu aksi pada baris `Door Antenna {runId}-058`, klik `Edit`
24. Klik `[Clear Field]`
25. Klik `[Save]`
26. Verifikasi field Device Name, Measurement, dan Category memiliki label yang terbaca screen reader
27. Verifikasi field Device Name, Measurement, dan Category memiliki atribut aria-required bernilai true
28. Verifikasi field yang berisi error memiliki atribut aria-describedby yang menunjuk ke pesan error inline
29. Tekan `Tab` berulang sampai fokus berputar
30. Verifikasi fokus Tab berputar di dalam popup dan tidak keluar ke halaman di belakangnya
31. Klik icon close `[✕]` pada popup
32. Verifikasi dialog `Unsaved Changes` tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" serta tombol `[Cancel]` dan `[Leave]`
33. Klik `[Leave]` pada dialog

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (Search `{runId}-058`) menemukan baris record milik spec dan tidak memuat asersi. Search dianggap tetap aktif sesudah popup Edit disimpan atau ditutup; spec tidak mengulang Search per blok.
- Record milik spec (S-06, S-12): R1 sampai R3 menggantikan `Cable Tester`, `RFID Reader`, dan `Door Antenna` Pre-setup #16; TC-AC-DN-134 dan TC-AC-DN-136 memakai R1 berurutan karena keduanya aksi no-op yang tidak mengubah record. Record Pre-setup #16 tidak diubah, sehingga nilai literal Last Modified Pre-setup #19 tidak dipakai dan Last Modified dibandingkan dengan nilai yang dicatat spec.
- Langkah penghubung (S-03): langkah 2 mencatat Last Modified sebelum aksi sebagai pembanding; langkah 31 sampai 33 menutup form dirty TC-AC-DN-180 secara deterministik (S-08).
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-134, TC-AC-DN-135, TC-AC-DN-136 (tidak ada entri log baru di Changelog, Activity Log, dan System Log aktor).
  - TC-AC-DN-134 dan TC-AC-DN-136 menyebut Last Modified tetap `10/09/26 12:25` dan TC-AC-DN-135 `01/09/26 06:00` untuk record Pre-setup #16; spec memakai record milik spec sehingga asersi "tetap" dibandingkan dengan nilai yang dicatat sebelum aksi.
  - TC-AC-DN-134 hingga TC-AC-DN-180: TC sumber menyebut nama record Pre-setup #16 dan teks tanpa suffix; spec memakai nama bersuffix `{runId}-<NNN>` (S-12) pada seed, input, dan asersi, dan mengikuti teks UI TC persis.
