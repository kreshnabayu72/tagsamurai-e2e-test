---
id: TC-AC-DC-E2E-083-log-absence-no-op-dan-gagal
title: "Absence Log: Save Tanpa Perubahan dan Edit No-op Tidak Menulis Entri"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DC-112
  - TC-AC-DC-113
  - TC-AC-DC-223
coverage:
  web: automated
---

# Absence Log: Save Tanpa Perubahan dan Edit No-op Tidak Menulis Entri

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control #1 (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Budi Santoso), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture backend (disediakan tim FE/BE; endpoint tidak dikarang di spec ini). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: pohon Pre-setup #14 (`Hardware` > `Handheld Reader`) hanya dibaca sebagai induk node milik spec dan tidak diubah.
- Data Dinamis (suffix `{runId}-083`): `Noop Uji {runId}-083` (leaf di bawah `Handheld Reader`), dibuat lewat sesi API aktor di hook `before` dan menjadi target ketiga TC. Nama tidak berubah di seluruh spec.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Noop Uji {runId}-083` bila masih ada. Entri log tidak dapat dihapus; nama bersuffix run.
- Kemampuan teknis (disediakan tim FE/BE; tanpa endpoint karangan): membaca jumlah total entri Changelog Category, System Log akun aktor, dan Activity Log Admin Console sebagai baseline sebelum dan sesudah aksi (B112, B113, B223 pada langkah 2, 9, dan 15); ketiganya audit trail permanen sehingga tidak diasersi sebagai angka absolut (S-12). Membuka Detail User akun aktor tab System Log dan Activity Log Admin Console.
- State global: tidak ada yang diubah.

## Test Steps

### TC-AC-DC-112: Save tanpa perubahan: toast netral dan tanpa entri log

1. Expand `Hardware`, lalu expand `Handheld Reader`
2. Baca dan catat jumlah entri Changelog Category, System Log akun aktor, dan Activity Log sebagai B112 (kemampuan baca)
3. Hover node `Noop Uji {runId}-083`, lalu klik aksi Edit
4. Tanpa mengubah nilai, klik `[Save]`
5. Verifikasi toast netral (Info) "No changes to save."
6. Verifikasi input inline Edit tertutup
7. Verifikasi nama node tetap "Noop Uji {runId}-083"
8. Verifikasi jumlah entri Changelog Category, System Log akun aktor, dan Activity Log sama dengan B112 (tidak ada entri baru)

### TC-AC-DC-113: Save yang hanya mengubah spasi tepi diperlakukan sebagai no-op

9. Baca dan catat jumlah entri Changelog Category, System Log akun aktor, dan Activity Log sebagai B113 (kemampuan baca)
10. Hover node `Noop Uji {runId}-083`, lalu klik aksi Edit
11. Ganti nilai dengan "  Noop Uji {runId}-083  " (spasi di awal dan akhir), lalu klik `[Save]`
12. Verifikasi toast netral "No changes to save."
13. Verifikasi nama node tetap "Noop Uji {runId}-083"
14. Verifikasi jumlah entri Changelog Category, System Log akun aktor, dan Activity Log sama dengan B113 (tidak ada entri baru di ketiga surface)

### TC-AC-DC-223: Edit no-op tidak menulis entri di Changelog, System Log, maupun Activity Log

15. Baca dan catat jumlah entri Changelog Category, System Log akun aktor, dan Activity Log sebagai B223 (kemampuan baca)
16. Hover node `Noop Uji {runId}-083`, lalu klik aksi Edit
17. Tanpa mengubah nilai, klik `[Save]`
18. Verifikasi toast netral (Info) "No changes to save."
19. Klik ikon Changelog pada header Sidebar Category
20. Verifikasi tabel Changelog menampilkan sedikitnya satu baris
21. Verifikasi jumlah entri Changelog Category sama dengan B223 (kemampuan baca)
22. Tutup modal Changelog lewat `[×]`
23. Buka Detail User akun aktor, lalu buka tab System Log
24. Verifikasi tabel System Log menampilkan sedikitnya satu baris
25. Verifikasi System Log akun aktor tidak memiliki entri baru dibanding B223 (kemampuan baca)
26. Buka Activity Log Admin Console
27. Verifikasi tabel Activity Log menampilkan sedikitnya satu baris
28. Verifikasi Activity Log tidak memiliki entri baru dibanding B223 (kemampuan baca)

## Notes

- P-5 (a): spec ini spec absence (kelas g); pemicunya (Save tanpa perubahan) hanya membentuk kondisi yang diasersi tidak tercatat dan tiap TC punya baseline sendiri.
- Anchor absence (bagian 8b butir 2): pada TC-AC-DC-112 dan 113, toast netral hasil server yang sudah diasersi (langkah 5 dan 12) dan baseline jumlah entri sebelum dan sesudah menjadi anchor; pada TC-AC-DC-223 tiap surface didahului `Verifikasi` tabel menampilkan sedikitnya satu baris (langkah 20, 24, 27) sebagai anchor positif untuk surface itu.
- Langkah penghubung (S-03): langkah 22 (menutup modal Changelog sebelum membuka surface lain). Asersi 223 memakai selisih jumlah entri terhadap baseline lewat kemampuan baca; tabel pada UI diamati hanya sebagai anchor.
- Pembagian TC lintas spec: Save no-op yang menjadi bagian alur TC lain, Delete diblok, dan request gagal ada di spec 084 dan 098; TC-AC-DC-230 (aksi pada satu node tidak menghasilkan entri node lain) ada di spec 097; pencatatan presence ada di spec 079 sampai 082 (S-05).
- Temuan untuk QA:
  - TC-AC-DC-112 dan 223 menyatakan "Changelog tetap N entri (baris teratas tidak berubah dan halaman 2 tetap berisi 2 baris)" dan "tidak ada entri baru" pada System Log dan Activity Log tanpa cara membaca jumlah di UI. Karena audit trail permanen, spec memakai selisih terhadap baseline lewat kemampuan baca yang disediakan tim FE/BE, bukan angka absolut atau posisi halaman (S-12, S-14).
  - TC-AC-DC-112 dan 223 hampir identik (Save tanpa perubahan pada node yang sama dan Expected "tidak ada entri baru" di tiga surface); TC-AC-DC-223 hanya menambah pembukaan UI System Log dan Activity Log.
  - TC memakai node literal Pre-setup #14 (`Rugged Scanner`) sebagai target; spec memakai node bersuffix milik spec (keputusan data tulis).
