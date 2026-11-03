---
id: TC-FA-FAAM-E2E-251-pencatatan-absence-bulk-delete-langsung-semua-in-use
title: "Pencatatan Absence: Request Bulk Delete Langsung Semua In-Use Tidak Menulis Entri di Changelog, System Log, dan Activity Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-844
coverage:
  web: automated
---

# Pencatatan Absence: Request Bulk Delete Langsung Semua In-Use Tidak Menulis Entri di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor UI (pengamat Changelog, System Log, dan Activity Log FAMS): Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Sesi API aktor pengirim request langsung (login API password, token tidak dihitung sebagai sesi web; disediakan tim BE/FE): Total Control client utama (`Spectra.env.FA_TC_PASSWORD`). Klien HTTP untuk request langsung disediakan tim BE/FE; endpoint tidak disebut TC dan tidak dikarang spec.
- Env var: `FA_TC_PASSWORD`.
- Data Dinamis, di-seed lewat API di hook `before`, nama bersuffix `{runId}-251`: `Bulk Used X 844 {runId}-251` (Total Asset 3) dan `Bulk Used Y 844 {runId}-251` (Total Asset 1; salinan fixture 14o, in-use).
- Kemampuan teknis: membuka Modal Changelog dan Search di dalamnya; membuka Detail User aktor tab System Log dan Activity Log FAMS beserta Search di dalamnya; membaca jumlah entri hasil Search di ketiganya sebelum aksi (baseline). Ketiganya adalah audit trail permanen sehingga hanya selisih terhadap baseline yang diasersi, bukan total absolut. Klien HTTP request langsung.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus seed milik spec ini lewat API.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition: pengamat UI Total Control berada di Fixed Asset > Settings > Asset Master > Asset Name; sesi API Total Control client utama.

## Test Steps

### TC-FA-FAAM-844: Request Bulk Delete langsung semua in-use tidak menulis entri di tiga surface log

1. Klik icon Changelog
2. Ketik Search `Bulk Used X 844 {runId}-251`, tekan Enter
3. Catat jumlah baris Changelog `Bulk Used X 844 {runId}-251` sebagai baseline
4. Ketik Search `Bulk Used Y 844 {runId}-251`, tekan Enter
5. Catat jumlah baris Changelog `Bulk Used Y 844 {runId}-251` sebagai baseline
6. Tutup Modal Changelog
7. Buka Detail User aktor lalu tab System Log
8. Ketik Search `Bulk Used X 844 {runId}-251`, tekan Enter
9. Catat jumlah entri System Log `Bulk Used X 844 {runId}-251` sebagai baseline
10. Ketik Search `Bulk Used Y 844 {runId}-251`, tekan Enter
11. Catat jumlah entri System Log `Bulk Used Y 844 {runId}-251` sebagai baseline
12. Buka Activity Log FAMS
13. Ketik Search `Bulk Used X 844 {runId}-251`, tekan Enter
14. Catat jumlah entri Activity Log FAMS `Bulk Used X 844 {runId}-251` sebagai baseline
15. Ketik Search `Bulk Used Y 844 {runId}-251`, tekan Enter
16. Catat jumlah entri Activity Log FAMS `Bulk Used Y 844 {runId}-251` sebagai baseline
17. Kirim request langsung ke server: Bulk Delete `Bulk Used X 844 {runId}-251` dan `Bulk Used Y 844 {runId}-251`
18. Verifikasi respons 200 dengan deleted 0 dan skipped 2
19. Buka Fixed Asset > Settings > Asset Master > Asset Name dan muat ulang List
20. Klik icon Changelog
21. Ketik Search `Bulk Used X 844 {runId}-251`, tekan Enter
22. Verifikasi jumlah baris Changelog `Bulk Used X 844 {runId}-251` sama dengan baseline pada langkah 3 (TC-FA-FAAM-844 butir b)
23. Ketik Search `Bulk Used Y 844 {runId}-251`, tekan Enter
24. Verifikasi jumlah baris Changelog `Bulk Used Y 844 {runId}-251` sama dengan baseline pada langkah 5 (TC-FA-FAAM-844 butir b)
25. Tutup Modal Changelog
26. Buka Detail User aktor lalu tab System Log
27. Ketik Search `Bulk Used X 844 {runId}-251`, tekan Enter
28. Verifikasi jumlah entri System Log `Bulk Used X 844 {runId}-251` sama dengan baseline pada langkah 9 (TC-FA-FAAM-844 butir c)
29. Ketik Search `Bulk Used Y 844 {runId}-251`, tekan Enter
30. Verifikasi jumlah entri System Log `Bulk Used Y 844 {runId}-251` sama dengan baseline pada langkah 11 (TC-FA-FAAM-844 butir c)
31. Buka Activity Log FAMS
32. Ketik Search `Bulk Used X 844 {runId}-251`, tekan Enter
33. Verifikasi jumlah entri Activity Log FAMS `Bulk Used X 844 {runId}-251` sama dengan baseline pada langkah 14 (TC-FA-FAAM-844 butir d)
34. Ketik Search `Bulk Used Y 844 {runId}-251`, tekan Enter
35. Verifikasi jumlah entri Activity Log FAMS `Bulk Used Y 844 {runId}-251` sama dengan baseline pada langkah 16 (TC-FA-FAAM-844 butir d)

## Notes

- P-5(a): spec ini kelas g; pemicu kelas a (Bulk Delete langsung semua in-use: TC-FA-FAAM-844) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji. Seed dan baseline milik spec ini sendiri.
- Langkah 18 (respons 200 dengan deleted 0 dan skipped 2) menjadi anchor positif bahwa pemicu benar-benar mencapai server sebelum asersi absence berikutnya; pembanding tiap surface adalah jumlah awal yang dicatat pada langkah baseline.
- Langkah penghubung tanpa `Verifikasi`: seluruh langkah selain langkah berawalan `Verifikasi`, yaitu membuka dan mencari di Modal Changelog, Detail User aktor tab System Log, dan Activity Log FAMS (S-12, S-14), mencatat baseline, navigasi, mengirim pemicu, dan menutup form dirty secara deterministik (S-08).
- Urutan: seluruh nama dicatat pada tiga surface sebelum request, lalu pemicu, lalu pengamatan tiga surface.
- Pembagian TC lintas spec: butir status respons dan state data TC-FA-FAAM-844 ada pada TC-FA-FAAM-631 (spec 248). TC-FA-FAAM-611 sampai 614 tetap di spec 247 bersama sisi presence di spec 231.
- Temuan untuk QA:
  - TC-FA-FAAM-844 meminta hitungan entri System Log dan Activity Log FAMS "yang memuat nama itu" lewat Search; TC tidak menyebut apakah tab System Log pada Detail User memiliki Search. Spec memakai Search pada ketiga surface; bila System Log tidak punya Search, hitungan perlu didefinisikan ulang.
