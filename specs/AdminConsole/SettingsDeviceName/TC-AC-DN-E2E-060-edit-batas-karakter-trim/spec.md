---
id: TC-AC-DN-E2E-060-edit-batas-karakter-trim
title: "Edit Device Name: Trim, 120 dan 121 Karakter, serta Spasi Melewati Batas"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DN-139
  - TC-AC-DN-140
  - TC-AC-DN-141
  - TC-AC-DN-142
coverage:
  web: automated
---

# Edit Device Name: Trim, 120 dan 121 Karakter, serta Spasi Melewati Batas

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap yang dirujuk spec: email akun Pre-setup #1, Measurement master `Unit`, `Meter`, `Box`, serta nama node pohon Category. Nama record dinamis dibentuk `<nama dasar> {runId}-060` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja, tidak diubah): #13 Measurement `Unit`, `Meter`, `Box`; #14 Pohon Category (`Hardware` > `Smart Fixed Reader` > `Antenna`; `Hardware` > `Handheld Reader` > `UHF Handheld`; `TAG` > `NFC` > `Accessory`, `Tag`); #20 General Settings (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Record inti Pre-setup #16 tidak menjadi target aksi; target aksi memakai record milik spec di bawah (S-06).
- Data Dinamis (milik spec; dibuat lewat API di hook `before`, dihapus di hook `after` termasuk hasil rename; kemampuan seeding Device Name disediakan tim FE/BE). Last Modified record seed berisi waktu pembuatan karena belum ada entri Changelog.

  | Kode | Nama awal | Measurement | Category | SKU | Dipakai oleh |
  |---|---|---|---|---|---|
  | R1 | `Door Antenna {runId}-060` | `Unit` | `Antenna` | tanpa SKU | TC-AC-DN-141, TC-AC-DN-139 |
  | R2 | `Door Pintu {runId}-060` | `Unit` | `Antenna` | tanpa SKU | TC-AC-DN-140, TC-AC-DN-142 |

- Nilai uji panjang (dihitung termasuk suffix): `Nama120A` = awalan `Alat Pemindai Gudang Besar ` diulang lalu dipotong sehingga bersama akhiran ` {runId}-060` panjang total tepat 120 karakter; `Nama121` = `Nama120A` ditambah satu karakter `Q` (121 karakter); `Nama120B` = awalan `Pintu Pemindai Gudang Kecil ` dengan perlakuan sama, tepat 120 karakter. Nilai ini dihitung hook `before` dari `{runId}`.
- Kemampuan teknis: mengetik, menempel, memilih opsi dropdown dan node pohon Category, menekan Esc dan Tab, serta klik area gelap di luar popup.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Search `{runId}-060` yang aktif sepanjang spec dipulihkan (dikosongkan) bila langkah berikutnya bergantung pada daftar penuh.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Ketik Search `{runId}-060`, tekan Enter

### TC-AC-DN-141: 121 karakter menampilkan error batas karakter dan Save tertahan

2. Buka menu aksi pada baris `Door Antenna {runId}-060`, klik `Edit`
3. Kosongkan field Device Name lalu ketik `Nama121` (121 karakter)
4. Verifikasi error inline "Max. 120 characters" muncul langsung saat karakter ke-121 diketik
5. Klik `[Save]`
6. Verifikasi error inline "Max. 120 characters" tetap tampil
7. Verifikasi popup form tetap terbuka
8. Verifikasi tidak ada toast
9. Klik icon close `[✕]` pada popup
10. Verifikasi dialog `Unsaved Changes` tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" serta tombol `[Cancel]` dan `[Leave]`
11. Klik `[Leave]` pada dialog

### TC-AC-DN-139: Spasi di awal dan akhir menyimpan nilai ter-trim

12. Buka menu aksi pada baris `Door Antenna {runId}-060`, klik `Edit`
13. Kosongkan field Device Name lalu ketik "   Door Trim {runId}-060   " (tiga spasi di awal dan di akhir)
14. Verifikasi tidak ada pesan error saat mengetik spasi di ujung
15. Klik `[Save]`
16. Verifikasi toast sukses "Success, device name has been updated."
17. Verifikasi List memuat baris dengan nama `Door Trim {runId}-060` tanpa spasi di awal atau akhir

### TC-AC-DN-140: Device Name tepat 120 karakter berhasil

18. Buka menu aksi pada baris `Door Pintu {runId}-060`, klik `Edit`
19. Kosongkan field Device Name lalu ketik `Nama120A` (120 karakter)
20. Verifikasi tidak ada error `Max. 120 characters`
21. Klik `[Save]`
22. Verifikasi toast sukses "Success, device name has been updated."
23. Verifikasi sel Device Name baris tersebut menampilkan `Nama120A` utuh 120 karakter tanpa pemotongan

### TC-AC-DN-142: Spasi di akhir yang melewati 120 karakter tidak memicu error

24. Buka menu aksi pada baris `Nama120A`, klik `Edit`
25. Kosongkan field Device Name lalu ketik `Nama120B` (120 karakter) diikuti lima spasi
26. Verifikasi tidak ada error `Max. 120 characters` karena panjang dihitung setelah trim
27. Klik `[Save]`
28. Verifikasi toast sukses "Success, device name has been updated."

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (Search `{runId}-060`) menemukan baris record milik spec dan tidak memuat asersi. Search dianggap tetap aktif sesudah popup Edit disimpan atau ditutup; spec tidak mengulang Search per blok.
- Record milik spec (S-06, S-12): R1 dan R2 menggantikan `Door Antenna` Pre-setup #16; R1 dipakai TC-AC-DN-141 (tidak tersimpan) lalu TC-AC-DN-139, R2 dipakai TC-AC-DN-140 lalu TC-AC-DN-142 (nama R2 sudah `Nama120A` sehingga TC-AC-DN-142 memakai `Nama120B` yang berbeda agar tidak menjadi aksi no-op). Record Pre-setup #16 tidak diubah, sehingga nilai literal Last Modified Pre-setup #19 tidak dipakai dan Last Modified dibandingkan dengan nilai yang dicatat spec.
- Penyimpangan urutan (S-10): TC-AC-DN-141 yang diblokir ditaruh sebelum blok yang menyimpan; TC-AC-DN-139 mengikuti karena memakai record yang sama.
- Langkah penghubung (S-03, S-08): langkah 9 sampai 11 menutup form dirty TC-AC-DN-141 secara deterministik (`[✕]`, dialog `Unsaved Changes`, `[Leave]`).
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-139 (nama tersimpan ter-trim), TC-AC-DN-140, TC-AC-DN-141, TC-AC-DN-142.
  - TC-AC-DN-140 dan TC-AC-DN-141 memberi nama 120 dan 121 karakter literal; spec membentuk nama yang diakhiri `{runId}-060` dan menghitung panjang termasuk suffix (R-06).
  - TC-AC-DN-139 hingga TC-AC-DN-142: TC sumber menyebut nama record Pre-setup #16 dan teks tanpa suffix; spec memakai nama bersuffix `{runId}-<NNN>` (S-12) pada seed, input, dan asersi, dan mengikuti teks UI TC persis.
