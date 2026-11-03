---
id: TC-AC-DC-E2E-084-log-absence-delete-diblok-dan-kegagalan
title: "Absence Log: Delete Diblok Referensi dan Delete Family Gagal Tidak Menulis Entri"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DC-220
  - TC-AC-DC-221
coverage:
  web: automated
---

# Absence Log: Delete Diblok Referensi dan Delete Family Gagal Tidak Menulis Entri

## Prerequisites

- Mode: FE+BE. Intercept parsial `Spectra.intercept()` di atas backend nyata dipakai pada langkah 12 sampai 16 (respons 500 untuk request hapus Category); endpoint tidak dikarang di spec ini.
- Akun aktor: Total Control #1 (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Budi Santoso), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture backend (disediakan tim FE/BE). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: pohon Pre-setup #14 (`Hardware` > `Handheld Reader`) hanya dibaca sebagai induk node milik spec dan tidak diubah.
- Data Dinamis (suffix `{runId}-084`), dibuat lewat sesi API aktor di hook `before`:
  - `Dipakai Uji {runId}-084` (leaf di bawah `Handheld Reader`) dan Device Name `HR-Uji {runId}-084` yang merujuknya (Category = `Dipakai Uji {runId}-084`), target TC-AC-DC-220.
  - Family `Keluarga Gagal {runId}-084` di bawah `Handheld Reader` dengan anak `Anak A Keluarga Gagal {runId}-084` (leaf) dan `Anak B Keluarga Gagal {runId}-084` yang memiliki anak `Cucu Keluarga Gagal {runId}-084`, target TC-AC-DC-221.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh; urutan: Device Name dahulu, lalu node): hapus lewat API `HR-Uji {runId}-084`, `Dipakai Uji {runId}-084`, dan family `Keluarga Gagal {runId}-084` beserta anak bila masih ada; lepas intercept bila belum dilepas.
- Kemampuan teknis (disediakan tim FE/BE; tanpa endpoint karangan): membaca jumlah total entri Changelog Category, System Log akun aktor, dan Activity Log Admin Console sebagai baseline sebelum dan sesudah aksi (B220 dan B221 pada langkah 2 dan 11); ketiganya audit trail permanen sehingga tidak diasersi sebagai angka absolut (S-12).
- State global: tidak ada yang diubah.

## Test Steps

### TC-AC-DC-220: Delete diblok referensi tidak menulis entri log di surface mana pun

1. Expand `Hardware`, lalu expand `Handheld Reader`
2. Baca dan catat jumlah entri Changelog Category, System Log akun aktor, dan Activity Log sebagai B220 (kemampuan baca)
3. Hover node `Dipakai Uji {runId}-084`, lalu klik aksi Delete
4. Verifikasi dialog blok "Cannot Delete Category" memuat bullet `HR-Uji {runId}-084` dan satu tombol `[OK]`
5. Klik `[OK]` pada dialog blok
6. Klik ikon Changelog pada header Sidebar Category
7. Verifikasi tabel Changelog menampilkan sedikitnya satu baris
8. Verifikasi jumlah entri Changelog Category sama dengan B220 (tanpa entri Delete baru)
9. Tutup modal Changelog lewat `[×]`
10. Verifikasi jumlah entri System Log akun aktor dan Activity Log sama dengan B220 (tidak bertambah)

### TC-AC-DC-221: Transaksi Delete family gagal menghasilkan nol entri log

11. Baca dan catat jumlah entri Changelog Category, System Log akun aktor, dan Activity Log sebagai B221 (kemampuan baca)
12. Pasang intercept: request hapus Category dipaksa mengembalikan error 500
13. Hover node `Keluarga Gagal {runId}-084`, lalu klik aksi Delete
14. Klik `[Delete]` pada dialog konfirmasi
15. Verifikasi toast error "Error, failed to delete category."
16. Lepas intercept
17. Expand `Keluarga Gagal {runId}-084`, lalu expand `Anak B Keluarga Gagal {runId}-084`
18. Verifikasi seluruh family tetap ada: `Keluarga Gagal {runId}-084`, `Anak A Keluarga Gagal {runId}-084`, `Anak B Keluarga Gagal {runId}-084`, dan `Cucu Keluarga Gagal {runId}-084` tampil di sidebar
19. Klik ikon Changelog pada header Sidebar Category
20. Verifikasi tabel Changelog menampilkan sedikitnya satu baris
21. Verifikasi jumlah entri Changelog Category sama dengan B221 (kemampuan baca)
22. Tutup modal Changelog lewat `[×]`
23. Verifikasi jumlah entri System Log akun aktor dan Activity Log sama dengan B221 (tidak bertambah)

## Notes

- P-5 (a): spec ini spec absence (kelas g); pemicu kelas b (respons 500 untuk TC-AC-DC-221) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC punya baseline sendiri. Intercept dilepas segera setelah toast diasersi (S-09).
- Anchor absence (bagian 8b butir 2): pada TC-AC-DC-220 dialog blok (langkah 4) dan surface Changelog termuat (langkah 7) menjadi anchor; pada TC-AC-DC-221 toast error (langkah 15), family yang tetap ada (langkah 18), dan surface Changelog termuat (langkah 20) menjadi anchor. Untuk System Log dan Activity Log, anchor adalah surface agregat: jumlah total sebelum dan sesudah (B220 dan B221), karena pemicu tidak menyentuh entitas yang dapat dijadikan anchor di UI kedua surface itu.
- Penyimpangan dari TC (S-03): `Verifikasi` dialog blok pada langkah 4 tidak ada di Expected TC-AC-DC-220 dan ditambahkan sebagai anchor positif untuk asersi absence (langkah 3 TC hanya menyebut "dialog konfirmasi tampil" dan langkah 4 menekan `[OK]` pada dialog blok). Isi dialog mengikuti Expected TC-AC-DC-235 dan 271.
- Langkah penghubung (S-03): langkah 5 dan 9 (menutup dialog dan modal), 16 (melepas intercept), 17 (membuka family untuk asersi).
- Pembagian TC lintas spec: TC-AC-DC-222 (Add dan Edit gagal) ada di spec 098; Save tanpa perubahan di spec 083; presence log di spec 079 sampai 082 (S-05).
- Temuan untuk QA:
  - TC-AC-DC-220 dan 221 Expected menulis "Changelog tetap 12 entri (baris teratas tidak berubah dan halaman 2 tetap berisi 2 baris)"; spec memakai selisih terhadap baseline lewat kemampuan baca karena audit trail permanen (S-12, S-14). Cara membaca jumlah entri System Log dan Activity Log di UI tidak disebut TC.
  - TC-AC-DC-220 memakai Device Name Pre-setup #15 (`HR-100`, Category `Dipakai Leaf`) dan node literal Pre-setup #14; spec memakai node dan Device Name bersuffix milik spec (keputusan data tulis). Device Name `HR-Uji {runId}-084` dibuat via API: field wajib Device Name lain tidak disebut TC dan disediakan tim FE/BE.
