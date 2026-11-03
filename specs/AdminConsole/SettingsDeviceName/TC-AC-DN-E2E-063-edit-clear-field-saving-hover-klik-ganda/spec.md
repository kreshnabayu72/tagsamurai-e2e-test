---
id: TC-AC-DN-E2E-063-edit-clear-field-saving-hover-klik-ganda
title: "Edit Device Name: Clear Field, Saving State, Hover Tombol, dan Klik Ganda Save"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-162
  - TC-AC-DN-163
  - TC-AC-DN-164
  - TC-AC-DN-165
  - TC-AC-DN-166
coverage:
  web: automated
---

# Edit Device Name: Clear Field, Saving State, Hover Tombol, dan Klik Ganda Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap yang dirujuk spec: email akun Pre-setup #1, Measurement master `Unit`, `Meter`, `Box`, serta nama node pohon Category. Nama record dinamis dibentuk `<nama dasar> {runId}-063` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja, tidak diubah): #13 Measurement `Unit`, `Meter`, `Box`; #14 Pohon Category (`Hardware` > `Smart Fixed Reader` > `Antenna`; `Hardware` > `Handheld Reader` > `UHF Handheld`; `TAG` > `NFC` > `Accessory`, `Tag`); #20 General Settings (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Record inti Pre-setup #16 tidak menjadi target aksi; target aksi memakai record milik spec di bawah (S-06).
- Data Dinamis (milik spec; dibuat lewat API di hook `before`, dihapus di hook `after` termasuk hasil rename; kemampuan seeding Device Name disediakan tim FE/BE). Last Modified record seed berisi waktu pembuatan karena belum ada entri Changelog.

  | Kode | Nama awal | Measurement | Category | SKU | Dipakai oleh |
  |---|---|---|---|---|---|
  | R1 | `Door Antenna {runId}-063` | `Unit` | `Antenna` | tanpa SKU | TC-AC-DN-162, TC-AC-DN-163, TC-AC-DN-165 |
  | R2 | `Door Antenna Dua {runId}-063` | `Unit` | `Antenna` | tanpa SKU | TC-AC-DN-164 |
  | R3 | `Door Antenna Tiga {runId}-063` | `Unit` | `Antenna` | tanpa SKU | TC-AC-DN-166 |

- Respons request penyimpanan pada TC-AC-DN-164 ditahan 5 detik lewat `Spectra.intercept()` di atas backend nyata untuk mengamati saving state (bukan kegagalan yang dipaksakan); intercept dilepas setelah asersi.
- Kemampuan teknis: `Spectra.intercept()` untuk menahan respons penyimpanan 5 detik, hover kursor pada tombol, dan klik ganda cepat (selang kurang dari 200 ms).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Search `{runId}-063` yang aktif sepanjang spec dipulihkan (dikosongkan) bila langkah berikutnya bergantung pada daftar penuh.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Ketik Search `{runId}-063`, tekan Enter

### TC-AC-DN-162: Tombol Clear Field mengosongkan semua field

2. Buka menu aksi pada baris `Door Antenna {runId}-063`, klik `Edit`
3. Klik `[Clear Field]`
4. Verifikasi field Device Name kosong dengan placeholder "Enter device name"
5. Verifikasi field Measurement kembali ke placeholder "Select measurement"
6. Verifikasi field Category kembali ke placeholder "Select category"
7. Verifikasi nilai tersimpan `Door Antenna {runId}-063`, `Unit`, dan `Antenna` tidak dikembalikan
8. Verifikasi popup tetap terbuka
9. Verifikasi fokus kursor berada di field Device Name
10. Verifikasi tidak ada dialog konfirmasi

### TC-AC-DN-163: Menutup form Edit setelah Clear Field

11. Klik icon close `[✕]` pada popup
12. Verifikasi dialog `Unsaved Changes` tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" serta tombol `[Cancel]` dan `[Leave]`
13. Verifikasi popup form Edit tetap terbuka di belakang dialog
14. Verifikasi field tetap kosong

### TC-AC-DN-165: Hover pada tombol Save dan Clear Field

15. Klik `[Cancel]` pada dialog
16. Arahkan kursor ke tombol `[Save]`
17. Verifikasi tombol `[Save]` menampilkan state hover yang berbeda dari state normal
18. Arahkan kursor ke tombol `[Clear Field]`
19. Verifikasi tombol `[Clear Field]` menampilkan state hover yang berbeda dari state normal
20. Klik icon close `[✕]` pada popup
21. Verifikasi dialog `Unsaved Changes` tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" serta tombol `[Cancel]` dan `[Leave]`
22. Klik `[Leave]` pada dialog

### TC-AC-DN-164: Saving state dan kontrol terkunci saat request berjalan

23. Buka menu aksi pada baris `Door Antenna Dua {runId}-063`, klik `Edit`
24. Kosongkan field Device Name lalu ketik "Door Saving {runId}-063"
25. Tahan respons request penyimpanan selama 5 detik lewat intercept jaringan
26. Klik `[Save]`
27. Verifikasi tombol `[Save]` menampilkan indikator loading
28. Verifikasi tombol `[Save]` berstatus disabled (tetap tampil)
29. Verifikasi tombol `[Clear Field]`, icon close `[✕]`, dan semua field berstatus disabled (tetap tampil)
30. Lepaskan tahanan respons (intercept dilepas)
31. Verifikasi popup tertutup
32. Verifikasi toast sukses "Success, device name has been updated."

### TC-AC-DN-166: Klik ganda cepat pada Save

33. Buka menu aksi pada baris `Door Antenna Tiga {runId}-063`, klik `Edit`
34. Kosongkan field Device Name lalu ketik "Door Double {runId}-063"
35. Klik `[Save]` dua kali dengan cepat (selang kurang dari 200 ms)
36. Verifikasi tombol `[Save]` berstatus disabled sejak klik pertama
37. Verifikasi satu toast sukses "Success, device name has been updated."
38. Verifikasi List memuat tepat satu baris `Door Double {runId}-063`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (Search `{runId}-063`) menemukan baris record milik spec dan tidak memuat asersi. Search dianggap tetap aktif sesudah popup Edit disimpan atau ditutup; spec tidak mengulang Search per blok.
- Record milik spec (S-06, S-12): R1 dipakai tiga TC tanpa Save; R2 dan R3 dibuat terpisah untuk TC yang menyimpan, menggantikan `Door Antenna` Pre-setup #16. Record Pre-setup #16 tidak diubah, sehingga nilai literal Last Modified Pre-setup #19 tidak dipakai dan Last Modified dibandingkan dengan nilai yang dicatat spec.
- Penyimpangan urutan (S-10): TC-AC-DN-165 (hover) ditaruh sebelum TC-AC-DN-164 dan TC-AC-DN-166 karena memakai popup R1 yang sudah dibuka untuk TC-AC-DN-162 dan TC-AC-DN-163 (satu pembukaan dipakai berulang); popup R1 ditutup di langkah 20 sampai 22 secara deterministik (`[✕]`, dialog `Unsaved Changes`, `[Leave]`) sebelum record lain dibuka. Langkah 15 (`[Cancel]`) adalah penghubung (S-03).
- Intercept ditahan hanya untuk mengamati saving state (bagian 6); dilepas pada langkah 30 sehingga tidak berlaku di blok berikutnya (S-09).
- Ukuran spec (38 langkah, di atas smell 35 langkah, kode R3): satu topik (kontrol dan state popup Edit), satu halaman, satu kelas harness; tiga record terpisah sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-166 (satu perubahan diproses dan satu entri log Edit tercatat, bukan dua).
  - TC-AC-DN-162 hingga TC-AC-DN-166: TC sumber menyebut nama record Pre-setup #16 dan teks tanpa suffix; spec memakai nama bersuffix `{runId}-<NNN>` (S-12) pada seed, input, dan asersi, dan mengikuti teks UI TC persis.
