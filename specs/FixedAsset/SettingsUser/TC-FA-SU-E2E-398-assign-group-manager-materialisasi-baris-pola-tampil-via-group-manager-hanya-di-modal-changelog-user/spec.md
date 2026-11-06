---
id: TC-FA-SU-E2E-398-assign-group-manager-materialisasi-baris-pola-tampil-via-group-manager-hanya-di-modal-changelog-user
title: "Assign Group Manager: Materialisasi Baris Pola Tampil sebagai Assign (via Group Manager) Hanya di Modal Changelog User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1097
coverage:
  web: automated
---

# Assign Group Manager: Materialisasi Baris Pola Tampil sebagai Assign (via Group Manager) Hanya di Modal Changelog User

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (Total Control). Halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite; spec ini berpindah ke halaman Settings > Role & Permission lewat langkah navigasi eksplisit (langkah 2) lalu kembali ke Settings > User (langkah 7).
- Hook suite (`suite.md`): flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23). Pengguna target: Wawan Setiawan (Home Group Finance & Accounting; tanpa status Group Manager, Pre-setup #48) yang ditugaskan sebagai Group Manager Finance & Accounting (turunan Accounts Payable). Nama pengguna dan grup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan baca jumlah entri (disediakan tim FE/BE): entri `Assign (via Group Manager)` pada modal Changelog User > Group Role dan > Transaction Role Wawan Setiawan, serta entri yang memuat `(via Group Manager)` pada modal Changelog User > Global Role, Tab Changelog Wawan Setiawan, Tab System Log aktor, dan Activity Log, dibaca sebelum aksi (baseline, S-12) dan sesudah aksi. Audit trail bersifat permanen sehingga asersi memakai selisih terhadap baseline. Entri muncul eventual: modal dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit (bagian 6).
- Kemampuan seed API (disediakan tim BE/FE): memulihkan status Group Manager dan baris pola Wawan Setiawan ke kondisi Pre-setup #48 (tanpa status Group Manager). Dijalankan sebagai langkah penghubung terakhir dan di hook `after` (cadangan).
- State yang diubah dan pemulihannya: Wawan Setiawan menjadi Group Manager Finance & Accounting dan baris pola ditulis (Last Updated dan Modified By berubah); entri log permanen bertambah. Dipulihkan lewat seed API. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Catat jumlah entri `Assign (via Group Manager)` pada modal Changelog User > Group Role dan > Transaction Role Wawan Setiawan, serta jumlah entri yang memuat `(via Group Manager)` pada modal Changelog User > Global Role, Tab Changelog Wawan Setiawan, Tab System Log aktor, dan Activity Log sebagai baseline
2. Buka Settings > Role & Permission lewat sidebar
3. Klik Tab Group Manager lalu pilih node Finance & Accounting
4. Klik `[+ Assign]`
5. Assign Wawan Setiawan
6. Tunggu aksi selesai
7. Buka Settings > User lewat sidebar
8. Ketik Search `Wawan Setiawan`, tekan Enter, lalu klik Name `Wawan Setiawan`
9. Klik Tab Role, klik Sub-tab Group Role, lalu klik Changelog icon
10. Muat ulang modal tiap 5 detik sampai entri `Assign (via Group Manager)` tampil (batas 2 menit)
11. Verifikasi jumlah entri `Assign (via Group Manager)` pada modal Group Role bertambah dibanding baseline
12. Verifikasi baris teratas sebanyak selisih (himpunan, urutan di antaranya tidak diasersi) masing-masing Action `Assign (via Group Manager)`, Field `[Role Name] — [Group Name]`, Old Value `—`, dan New Value `Assigned`
13. Verifikasi perubahan kolom C/U/D pada baris Group Role yang sudah aktif sebelum Assign dicatat satu entri `Edit` per kolom yang berubah
14. Buka Filter Action pada modal Group Role
15. Verifikasi Filter Action menawarkan opsi `Assign (via Group Manager)`
16. Ketik Search `via Group Manager`, tekan Enter
17. Verifikasi seluruh baris hasil Search hanya entri `Assign (via Group Manager)` (sedikitnya satu baris tampil)
18. Klik `(←)` pada kotak Search, tutup Filter Action, lalu tutup modal Changelog
19. Klik Sub-tab Transaction Role lalu klik Changelog icon
20. Muat ulang modal tiap 5 detik sampai entri `Assign (via Group Manager)` tampil (batas 2 menit)
21. Verifikasi jumlah entri `Assign (via Group Manager)` pada modal Transaction Role bertambah dibanding baseline
22. Verifikasi baris teratas sebanyak selisih (himpunan, urutan di antaranya tidak diasersi) masing-masing Action `Assign (via Group Manager)`, Field `[Transaction Type] — [Group Name] — [Role]`, Old Value `—`, New Value `Assigned`, dan Modified By `Ahmad D`
23. Buka Filter Action pada modal Transaction Role
24. Verifikasi Filter Action menawarkan opsi `Assign (via Group Manager)`
25. Ketik Search `via Group Manager`, tekan Enter
26. Verifikasi seluruh baris hasil Search hanya entri `Assign (via Group Manager)` (sedikitnya satu baris tampil)
27. Klik `(←)` pada kotak Search, tutup Filter Action, lalu tutup modal Changelog
28. Klik Sub-tab Global Role, klik Changelog icon, lalu baca jumlah entri yang memuat `(via Group Manager)` pada modal Global Role
29. Tutup modal Changelog, lalu baca jumlah entri yang memuat `(via Group Manager)` pada Tab Changelog Wawan Setiawan, Tab System Log aktor, dan Activity Log
30. Verifikasi jumlah entri yang memuat `(via Group Manager)` sama dengan baseline pada modal Changelog User > Global Role, Tab Changelog, Tab System Log aktor, dan Activity Log
31. Pulihkan status Group Manager dan baris pola Wawan Setiawan ke Pre-setup #48 lewat seed API

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Langkah 1 TC ("Login sebagai Ahmad Dahlan") dilakukan hook `before`.
- Urutan langkah 3 sampai 6 TC diubah: Filter Action dan Search `via Group Manager` (langkah 6 TC, Expected d) dijalankan pada tiap modal segera setelah modal dibuka (langkah 14 sampai 18 dan 23 sampai 27) supaya modal tidak dibuka dua kali; langkah 4 TC (tutup modal lalu Sub-tab Transaction Role) menjadi langkah 18 sampai 19; langkah 5 TC (modal Global Role, Tab Changelog, System Log, Activity Log) menjadi langkah 28 sampai 30.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (baseline), 2 (navigasi ke Role & Permission; halaman ini berbeda dari halaman `beforeEach` suite, S-14), 6 (tunggu aksi selesai karena langkah berikutnya berpindah surface), 7, 8 (Search untuk menemukan baris target, R-16 dan R-23), 10 dan 20 (polling idiom bagian 6, sesuai langkah 6 TC "tunggu atau refresh sampai entri tampil"), 18 dan 27 (bersihkan Search, tutup modal), 29, dan 31 (pemulihan).
- Asersi absence langkah 30 (bagian 8b butir 2): anchor positif terhubung ke pemicu adalah langkah 12 dan 22 (entri `Assign (via Group Manager)` tampil pada dua modal yang sama-sama bagian dari Changelog User Wawan Setiawan); perbandingan dengan baseline langkah 1 menjaga asersi dari entri `(via Group Manager)` yang sudah ada.
- Langkah 17 dan 26 ("hanya entri `Assign (via Group Manager)`") didahului langkah 12 dan 22 sebagai pembanding bahwa sedikitnya satu baris ada; asersi universal tidak lulus semu pada tabel kosong.
- Temuan untuk QA:
  - Langkah 2 TC ("klik `[+ Assign]` dan assign Wawan Setiawan") tidak menyebut cara memilih Wawan Setiawan dan tombol konfirmasi dialog; spec mengikuti TC pada langkah 5 tanpa mengarang elemen.
  - Pre-setup TC (kolom precondition c) tidak menyebut #48 padahal status "Wawan tanpa Group Manager" hanya ada di #48; spec menambahkannya di `## Prerequisites`.
  - Expected a menyebut baris pola yang sudah aktif dengan C/U/D berubah dicatat satu entri `Edit` per kolom, tetapi Pre-setup TC tidak menyebut baris Group Role Wawan mana yang sudah aktif dengan CRUD berapa; langkah 13 diasersi longgar (baris Group Role yang sudah aktif sebelum Assign, mis. Manage group pada Finance & Accounting) dan jumlah entri tidak diasersi. Belum jelas apakah baris pemicu `Edit` dicatat atau tidak; mohon konfirmasi.
  - Jumlah entri `Assign (via Group Manager)` yang diharapkan tidak disebut Expected a dan b ("per baris pola yang baru ditulis"); spec hanya mengasersi bertambah dibanding baseline.
  - Expected b menyebut "Modified By aktor"; spec memakai `Ahmad D` (format `[First Name] [Last Initial]`, R-14). Expected a tidak menyebut Modified By.
  - TC-FA-SU-1097 menyebut tombol `[Remove]` pada TC-FA-SU-294 sedangkan PRD DO-12 menyebut `[Revoke]`; tidak berdampak langsung di spec ini.
  - Email dan nama env password Wawan Setiawan tidak diperlukan (hanya target).
