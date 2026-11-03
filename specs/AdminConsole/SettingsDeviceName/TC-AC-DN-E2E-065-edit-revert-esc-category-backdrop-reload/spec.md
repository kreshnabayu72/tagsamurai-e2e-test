---
id: TC-AC-DN-E2E-065-edit-revert-esc-category-backdrop-reload
title: "Edit Device Name: Kembali ke Nilai Awal, Esc setelah Ubah Category, Backdrop, Navigasi In-app, dan Reload"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-175
  - TC-AC-DN-589
  - TC-AC-DN-590
  - TC-AC-DN-177
  - TC-AC-DN-178
  - TC-AC-DN-179
coverage:
  web: automated
---

# Edit Device Name: Kembali ke Nilai Awal, Esc setelah Ubah Category, Backdrop, Navigasi In-app, dan Reload

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap yang dirujuk spec: email akun Pre-setup #1, Measurement master `Unit`, `Meter`, `Box`, serta nama node pohon Category. Nama record dinamis dibentuk `<nama dasar> {runId}-065` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja, tidak diubah): #13 Measurement `Unit`, `Meter`, `Box`; #14 Pohon Category (`Hardware` > `Smart Fixed Reader` > `Antenna`; `Hardware` > `Handheld Reader` > `UHF Handheld`; `TAG` > `NFC` > `Accessory`, `Tag`); #20 General Settings (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Record inti Pre-setup #16 tidak menjadi target aksi; target aksi memakai record milik spec di bawah (S-06).
- Data Dinamis (milik spec; dibuat lewat API di hook `before`, dihapus di hook `after` termasuk hasil rename; kemampuan seeding Device Name disediakan tim FE/BE). Last Modified record seed berisi waktu pembuatan karena belum ada entri Changelog.

  | Kode | Nama awal | Measurement | Category | SKU | Dipakai oleh |
  |---|---|---|---|---|---|
  | R1 | `Door Antenna {runId}-065` | `Unit` | `Antenna` | tanpa SKU | TC-AC-DN-175, TC-AC-DN-589, TC-AC-DN-590, TC-AC-DN-177, TC-AC-DN-178, TC-AC-DN-179 |

- Tidak ada perubahan yang disimpan; popup R1 dibuka tiga kali dan ditutup tiga kali.
- Kemampuan teknis: menekan `F5` dan menangani konfirmasi `beforeunload` bawaan browser (membatalkan reload), klik area gelap di luar popup, klik breadcrumb, serta menekan Esc. Form dirty pada TC-AC-DN-179 ditutup deterministik sesudah reload dibatalkan (S-08).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Search `{runId}-065` yang aktif sepanjang spec dipulihkan (dikosongkan) bila langkah berikutnya bergantung pada daftar penuh.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Ketik Search `{runId}-065`, tekan Enter

### TC-AC-DN-175: Mengembalikan perubahan ke nilai awal membuat form bersih

2. Buka menu aksi pada baris `Door Antenna {runId}-065`, klik `Edit`
3. Kosongkan field Device Name lalu ketik "Door Antenna {runId}-065 X"
4. Hapus karakter ` X` sehingga isi field kembali `Door Antenna {runId}-065`
5. Klik icon close `[✕]` pada popup
6. Verifikasi popup form tertutup langsung
7. Verifikasi dialog `Unsaved Changes` tidak muncul

### TC-AC-DN-589: Esc setelah mengubah hanya Category, Cancel mempertahankan perubahan

8. Buka menu aksi pada baris `Door Antenna {runId}-065`, klik `Edit`
9. Klik field Category, expand `TAG` lalu `NFC`, pilih leaf `Tag`
10. Tekan `Esc`
11. Verifikasi dialog `Unsaved Changes` tampil dengan teks "You have unsaved changes. Are you sure you want to leave?" serta tombol `[Cancel]` dan `[Leave]`
12. Klik `[Cancel]` pada dialog
13. Verifikasi popup Edit tetap terbuka
14. Verifikasi field Category tetap menampilkan `Tag`

### TC-AC-DN-590: Esc setelah mengubah hanya Category, Leave menutup tanpa menyimpan

15. Tekan `Esc`
16. Verifikasi dialog `Unsaved Changes` tampil
17. Klik `[Leave]` pada dialog
18. Verifikasi dialog dan popup Edit tertutup
19. Verifikasi tidak ada toast
20. Verifikasi baris `Door Antenna {runId}-065` menampilkan Category badge `Antenna`

### TC-AC-DN-177: Klik backdrop pada form yang sudah diubah

21. Buka menu aksi pada baris `Door Antenna {runId}-065`, klik `Edit`
22. Kosongkan field Device Name lalu ketik "Door Draft"
23. Klik area gelap di luar popup
24. Verifikasi popup form Edit tetap terbuka dengan Device Name `Door Draft` dipertahankan
25. Verifikasi dialog `Unsaved Changes` tidak muncul

### TC-AC-DN-178: Navigasi in-app saat form diubah

26. Klik breadcrumb segmen tengah menuju halaman lain di aplikasi
27. Verifikasi perubahan halaman dicegat
28. Verifikasi dialog `Unsaved Changes` tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" serta tombol `[Cancel]` dan `[Leave]`
29. Klik `[Cancel]` pada dialog

### TC-AC-DN-179: Reload halaman saat form diubah

30. Tekan `F5`
31. Verifikasi konfirmasi bawaan browser (beforeunload) tampil sebelum halaman dimuat ulang
32. Batalkan reload pada konfirmasi bawaan browser sehingga tetap di halaman
33. Klik icon close `[✕]` pada popup
34. Verifikasi dialog `Unsaved Changes` tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" serta tombol `[Cancel]` dan `[Leave]`
35. Klik `[Leave]` pada dialog

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (Search `{runId}-065`) menemukan baris record milik spec dan tidak memuat asersi. Search dianggap tetap aktif sesudah popup Edit disimpan atau ditutup; spec tidak mengulang Search per blok.
- Record milik spec (S-06, S-12): R1 menggantikan `Door Antenna` Pre-setup #16 dan tidak pernah tersimpan berubah. Record Pre-setup #16 tidak diubah, sehingga nilai literal Last Modified Pre-setup #19 tidak dipakai dan Last Modified dibandingkan dengan nilai yang dicatat spec.
- Penyimpangan urutan (S-10): TC-AC-DN-590 melanjutkan popup TC-AC-DN-589 (Category sudah `Tag`, dialog ditutup `[Cancel]`) dan hanya mengulang `Esc`; TC-AC-DN-178 melanjutkan popup TC-AC-DN-177 (isian "Door Draft"), dan TC-AC-DN-179 melanjutkan popup yang sama. Jumlah buka form tidak lebih dari jumlah penutupan (S-10).
- Langkah penghubung (S-03): langkah 29 (`[Cancel]`) mengembalikan form dari dialog navigasi; langkah 33 sampai 35 menutup form dirty secara deterministik (S-08).
- Reload (S-08): konfirmasi `beforeunload` dibatalkan sehingga halaman tidak dimuat ulang; kemampuan menangani dialog browser tertulis di `## Prerequisites`.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-589, TC-AC-DN-590 (kolom Post Condition).
  - TC-AC-DN-178 menyebut "breadcrumb atau item sidebar"; spec memilih breadcrumb segmen tengah dan tidak menguji item sidebar.
  - TC-AC-DN-175 hingga TC-AC-DN-179: TC sumber menyebut nama record Pre-setup #16 dan teks tanpa suffix; spec memakai nama bersuffix `{runId}-<NNN>` (S-12) pada seed, input, dan asersi, dan mengikuti teks UI TC persis.
