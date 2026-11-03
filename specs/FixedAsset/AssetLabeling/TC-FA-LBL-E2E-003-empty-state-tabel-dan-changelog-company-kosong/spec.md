---
id: TC-FA-LBL-E2E-003-empty-state-tabel-dan-changelog-company-kosong
title: "Empty State Tabel dan Changelog (Company Kosong)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-11
  - TC-FA-LBL-287
  - TC-FA-LBL-530
  - TC-FA-LBL-531
coverage:
  web: automated
---

# Empty State Tabel dan Changelog (Company Kosong)

## Prerequisites

- Mode: FE+BE.
- Hook suite: `before`, `beforeEach`, dan `after` berlaku sesuai `suite.md` (termasuk flag Guided Tooltip `seen`); spec ini tidak menulis ulang isinya.
- Akun aktor: Total Control `Company Kosong` (Pre-setup #21, nol label dan nol entri log), `Fixture.assetLabeling.akun.totalControlKosong`, `Spectra.env.FA_TC_KOSONG_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Environment variable: `FA_TC_KOSONG_PASSWORD`, `FA_LBL_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Fixture: `Fixture.assetLabeling.*` (`fixtures/asset-labeling.json`) memuat identitas akun tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Data Pre-setup (dibaca saja, tidak diubah spec): #21 `Company Kosong`. Spec tidak membuat label dan tidak menghasilkan entri log; Company tetap kosong selama spec berjalan.
- State global: tidak ada yang diubah selain sesi login. Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-FA-LBL-11: Empty state genuinely saat client belum punya label

1. Verifikasi tabel menampilkan Illustration dengan Title `No labels yet` dan Description `Get started by creating your first label.`
2. Verifikasi tidak ada tombol CTA di dalam empty state
3. Verifikasi tombol `[+ Label]` di Table Tools tetap tampil

### TC-FA-LBL-530: Filter Panel Labels List pada sumber 0 baris: dropdown Modified By menampilkan No options available

4. Verifikasi tabel menampilkan empty state `No labels yet`
5. Klik icon Filter di Table Tools
6. Verifikasi Filter Panel terbuka dengan field `Total Asset`, `Modified By`, dan `Last Updated`
7. Buka dropdown `Modified By`
8. Verifikasi dropdown `Modified By` menampilkan teks `No options available` tanpa opsi
9. Verifikasi dropdown `Modified By` tidak menampilkan pesan error
10. Tutup dropdown `Modified By` dan Filter Panel

### TC-FA-LBL-287: Empty state genuinely Modal Changelog

11. Klik icon Changelog di Table Tools
12. Verifikasi Modal Changelog menampilkan Illustration dengan Title `No changelog yet` dan Description `Activities and changes will appear here.`

### TC-FA-LBL-531: Filter Panel Modal Changelog pada log kosong: dropdown Action, Label Name, Field, dan Modified By menampilkan No options available

13. Verifikasi Modal Changelog menampilkan empty state `No changelog yet`
14. Klik icon Filter di toolbar modal
15. Verifikasi Filter Panel terbuka dengan field `Date`, `Action`, `Label Name`, `Field`, dan `Modified By`
16. Buka dropdown `Action`
17. Verifikasi dropdown `Action` menampilkan teks `No options available`
18. Verifikasi dropdown `Action` tidak menampilkan pesan error
19. Tutup dropdown `Action`
20. Buka dropdown `Label Name`
21. Verifikasi dropdown `Label Name` menampilkan teks `No options available`
22. Verifikasi dropdown `Label Name` tidak menampilkan pesan error
23. Tutup dropdown `Label Name`
24. Buka dropdown `Field`
25. Verifikasi dropdown `Field` menampilkan teks `No options available`
26. Verifikasi dropdown `Field` tidak menampilkan pesan error
27. Tutup dropdown `Field`
28. Buka dropdown `Modified By`
29. Verifikasi dropdown `Modified By` menampilkan teks `No options available`
30. Verifikasi dropdown `Modified By` tidak menampilkan pesan error
31. Tutup dropdown `Modified By`, Filter Panel, dan Modal Changelog

## Notes

- Langkah penghubung (S-03): langkah 10 (menutup dropdown dan Filter Panel sebelum membuka Changelog), langkah 19, 23, 27, dan 31 (menutup dropdown, Filter Panel, dan modal setelah asersi).
- Modal Changelog dibuka sekali di langkah 11 dan dipakai bersama TC-FA-LBL-287 dan TC-FA-LBL-531 karena langkah pembukanya identik (TC-FA-LBL-531 langkah 1 sama dengan TC-FA-LBL-287 langkah 1); Verifikasi empty state tiap TC tetap ditulis sendiri (langkah 12 dan 13).
- Absence pada langkah 9, 18, 22, 26, dan 30 (tidak ada pesan error): teks `No options available` pada langkah sebelumnya pada dropdown yang sama menjadi anchor positif (bagian 8b butir 2).
- Temuan untuk QA: TC-FA-LBL-11 butir "tidak ada tombol CTA di dalam empty state" tidak menyebut elemen pembanding; spec memakai Illustration, Title, dan Description pada langkah 1 sebagai anchor.
