---
id: TC-AC-DN-E2E-181-konkurensi-edit-bagian-1
title: "Konkurensi Edit: Duplikat, Device Name Dihapus Admin Lain, dan Save setelah Device Name Terhapus"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DN-147
  - TC-AC-DN-573
  - TC-AC-DN-159
coverage:
  web: automated
---

# Konkurensi Edit: Duplikat, Device Name Dihapus Admin Lain, dan Save setelah Device Name Terhapus

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal; email dirujuk lewat `Fixture.settings-device-name.akunTotalControl`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Pelaku kedua: Maya Putri (Pre-setup #2) `totalControlDevName2_automated_{namaCompany}@qwertysystem.net` (Total Control, entitas Principal; email lewat `Fixture.settings-device-name.akunTotalControl2`), password `Spectra.env.AC_DN_TC2_PASSWORD` (belum terdaftar; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Pelaku kedua memakai sesi API (token tidak dihitung sebagai sesi web, lihat `suite.md`) hanya untuk memicu perubahan state; tidak ada sesi UI kedua.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap: email akun Pre-setup #1 dan #2, Measurement `Unit`, node pohon Category `Antenna`. Nama dinamis dibentuk `<nama dasar> {runId}-181` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja): #13 Measurement `Unit`; #14 Pohon Category (`Antenna`).
- Data Dinamis (milik spec; dibuat lewat API di hook `before`, dihapus di hook `after`; kemampuan seeding disediakan tim FE/BE). Seed tidak menulis entri Changelog.

  | Kode | Nama awal | Measurement | Category | Aksi pelaku kedua | Dipakai oleh |
  |---|---|---|---|---|---|
  | R1 | `Edit Dup {runId}-181` | `Unit` | `Antenna` | membuat Device Name `Race Edit {runId}-181` (Unit, Antenna) | TC-AC-DN-147 |
  | R2 | `Antenna Hapus {runId}-181` | `Unit` | `Antenna` | menghapus R2 | TC-AC-DN-573 |
  | R3 | `Door Asal {runId}-181` | `Unit` | `Antenna` | menghapus R3 | TC-AC-DN-159 |

- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `AC_TC_PASSWORD` (sudah terdaftar) dan `AC_DN_TC2_PASSWORD`.

## Test Steps

### TC-AC-DN-147: Save Edit ditolak sebagai duplikat setelah pengecekan lolos

1. Ketik Search `Edit Dup {runId}-181`, tekan Enter
2. Buka menu aksi pada baris `Edit Dup {runId}-181`, klik `Edit`
3. Kosongkan field Device Name lalu ketik "Race Edit {runId}-181"
4. Tunggu 500 ms
5. Maya Putri (sesi API) membuat Device Name `Race Edit {runId}-181` dengan Measurement `Unit` dan Category `Antenna` hingga tersimpan
6. Klik `[Save]`
7. Verifikasi error inline "Device name already exists" muncul di bawah field Device Name
8. Verifikasi popup form tetap terbuka
9. Verifikasi input Device Name dipertahankan
10. Kembalikan field Device Name ke nilai tersimpan `Edit Dup {runId}-181`
11. Klik icon `(✕)` pada form

### TC-AC-DN-573: Submit Edit setelah Device Name dihapus sesi lain

12. Ketik Search `Antenna Hapus {runId}-181`, tekan Enter
13. Buka menu aksi pada baris `Antenna Hapus {runId}-181`, klik `Edit`
14. Kosongkan field Device Name lalu ketik "Antenna Hapus Baru {runId}-181"
15. Maya Putri (sesi API) menghapus Device Name `Antenna Hapus {runId}-181` hingga terhapus
16. Klik `[Save]`
17. Verifikasi toast netral "This device name is no longer available."
18. Verifikasi form Edit ditutup
19. Verifikasi List tidak memuat "Antenna Hapus {runId}-181" maupun "Antenna Hapus Baru {runId}-181"

### TC-AC-DN-159: Save Edit pada Device Name yang sudah dihapus admin lain

20. Ketik Search `Door Asal {runId}-181`, tekan Enter
21. Buka menu aksi pada baris `Door Asal {runId}-181`, klik `Edit`
22. Kosongkan field Device Name lalu ketik "Door Gone {runId}-181"
23. Maya Putri (sesi API) menghapus Device Name `Door Asal {runId}-181` hingga terhapus
24. Klik `[Save]`
25. Verifikasi toast netral "This device name is no longer available."
26. Verifikasi popup form tertutup
27. Verifikasi List tidak memuat "Door Asal {runId}-181" maupun "Door Gone {runId}-181"

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pelaku kedua lewat sesi API bukan konteks kedua (tidak memakai P-2); langkah pemicu ditulis "... hingga ... tersimpan/terhapus" (R-20). Pembuatan dan penghapusan Device Name lewat sesi API adalah kemampuan yang disediakan tim FE/BE; TC menyebut jalur UI untuk langkah tersebut.
- Langkah penghubung (S-03, R-16): langkah 1, 12, 20 (Search) menemukan baris record milik spec; langkah 4 adalah jeda debounce 500 ms sesuai TC; langkah 10 dan 11 mengembalikan field ke nilai tersimpan dan menutup form (S-09, S-08: form tidak berisi perubahan sehingga tidak ada dialog `Unsaved Changes`).
- Anchor absence (8b butir 2): toast netral langkah 17 dan 25 adalah respons server yang selesai dan menjadi anchor langkah 19 dan 27. Nama yang dicari absence bukan substring nama lain pada tabel (R-13).
- Record milik spec (S-06, S-12): R1 sampai R3 menggantikan `Door Antenna` dan `Cable Tester` Pre-setup #16 TC sumber; Pre-setup #16 tidak diubah. TC-AC-DN-573 dan TC-AC-DN-159 memiliki alur yang hampir sama (Edit lalu hapus oleh sesi lain); tiap TC tetap satu spec ini.
- Urutan: mengikuti sourceTc; tiap blok menghapus recordnya sendiri sebagai bagian alur.
- Spec lain: TC-AC-DN-572 (dua sesi Edit ke nama yang sama) ada di spec 186.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-147 (record `Door Antenna` tidak berubah, hanya satu `Race Edit`), TC-AC-DN-573, TC-AC-DN-159.
  - TC memakai nama tanpa suffix; spec memakai nama bersuffix `{runId}-181` (S-12).
