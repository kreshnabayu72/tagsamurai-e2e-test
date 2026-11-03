---
id: TC-FA-SU-E2E-323-defense-in-depth-transaction-role-dan-group-role-target-tier-di-luar-scope-dan
title: "Defense-in-depth Transaction Role dan Group Role: Target Tier, Di Luar Scope, dan Perubahan Baris Terkunci"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-222
  - TC-FA-SU-223
  - TC-FA-SU-272
  - TC-FA-SU-1062
coverage:
  web: automated
---

# Defense-in-depth Transaction Role dan Group Role: Target Tier, Di Luar Scope, dan Perubahan Baris Terkunci

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage user & role Group (Update) Sinta Dewi (Pre-setup #6), email disediakan tim FE (tidak tertulis di Pre-setup TC), kredensial `Spectra.env.FA_MURGR_UPD_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun aktor berikutnya (ganti akun eksplisit, S-07): langkah 18 Group Manager (IT Infrastructure dan Accounts Payable) Oscar Pranata (Pre-setup #9; email disediakan tim FE; `Spectra.env.FA_GM_PASSWORD`); langkah 28 Manage global user & role (Update) Qori Akbar (Pre-setup #4; email disediakan tim FE; `Spectra.env.FA_MURG_UPD_PASSWORD`).
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Transaction Role (#39). Target: Wawan Setiawan, Yuda Pratama, Lina Marlina (Total Control, memiliki Transaction Role), Citra Lestari (Read Only), Ahmad Dahlan (Default User), Qori Akbar (akun sendiri). Semua blok ditolak server sehingga tidak ada data yang diubah.
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server; pembacaan state data (status aktif, nilai Global Role, penugasan Group Role dan Transaction Role, Home Group) lewat fixture BE.
- Ganti akun ke Oscar Pranata (langkah 18) memakai login UI karena sebelum dan sesudahnya ada langkah tampilan; ganti akun ke Qori Akbar (langkah 28) hanya mengambil token sesi API untuk klien HTTP (sesi UI tetap Oscar Pranata).
- State global dan pemulihan: tidak ada state global yang diubah dan tidak ada data yang diubah, sehingga tidak ada pemulihan. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-222: Perubahan paksa pada baris Group Role terkunci

1. Kirim permintaan langsung ke API ubah CRUD baris Branch Surabaya milik Wawan Setiawan (di luar scope Finance & Accounting) memakai klien HTTP dengan token sesi Sinta Dewi
2. Verifikasi server menolak permintaan dengan status 403 untuk baris di luar scope
3. Verifikasi nilai CRUD baris Branch Surabaya milik Wawan Setiawan tidak berubah (dibaca lewat API)

### TC-FA-SU-272: Permintaan paksa Assign atau Remove Transaction Role pada grup di luar scope

4. Kirim permintaan langsung ke API assign Transaction Role pada Logistics Warehouse (di luar scope) untuk Yuda Pratama memakai klien HTTP dengan token sesi Sinta Dewi
5. Verifikasi server menolak permintaan dengan status 403
6. Kirim permintaan langsung ke API remove baris Transaction Role Yuda Pratama yang memuat grup di luar scope memakai klien HTTP dengan token sesi Sinta Dewi
7. Verifikasi server menolak permintaan dengan status 403
8. Verifikasi penugasan Transaction Role Yuda Pratama tidak berubah (dibaca lewat API)

### TC-FA-SU-1062: Row action Remove dan checkbox target tier Disabled, Bulk Remove tidak dapat dipicu, dan permintaan remove ditolak

9. Ketik Search `Lina`, tekan Enter, klik nama Lina Marlina (Total Control), lalu buka Tab Role > Sub-tab Transaction Role
10. Hover row action `Remove` pada satu baris Lina Marlina
11. Verifikasi row action `Remove` baris Lina Marlina Disabled dengan tooltip "You don't have permission to edit."
12. Hover checkbox pada satu baris Lina Marlina
13. Verifikasi checkbox baris Lina Marlina Disabled dengan tooltip "You don't have permission to edit."
14. Verifikasi tidak ada baris terpilih dan `[Bulk Remove]` tidak dapat dipicu
15. Kirim permintaan langsung ke API remove Transaction Role untuk Lina Marlina memakai klien HTTP dengan token sesi Sinta Dewi
16. Verifikasi server menolak permintaan dengan status 403
17. Verifikasi tidak ada baris Transaction Role Lina Marlina yang terhapus (dibaca lewat API)
18. Ganti akun: logout, login sebagai Oscar Pranata (Group Manager (IT Infrastructure dan Accounts Payable), `Spectra.env.FA_GM_PASSWORD`), lalu buka Fixed Asset > Settings > User; klien HTTP memakai token sesi API akun yang sama
19. Ketik Search `Lina`, tekan Enter, klik nama Lina Marlina (Total Control), lalu buka Tab Role > Sub-tab Transaction Role
20. Hover row action `Remove` pada satu baris Lina Marlina
21. Verifikasi row action `Remove` baris Lina Marlina Disabled dengan tooltip "You don't have permission to edit."
22. Hover checkbox pada satu baris Lina Marlina
23. Verifikasi checkbox baris Lina Marlina Disabled dengan tooltip "You don't have permission to edit."
24. Verifikasi tidak ada baris terpilih dan `[Bulk Remove]` tidak dapat dipicu
25. Kirim permintaan langsung ke API remove Transaction Role untuk Lina Marlina memakai klien HTTP dengan token sesi Oscar Pranata
26. Verifikasi server menolak permintaan dengan status 403
27. Verifikasi tidak ada baris Transaction Role Lina Marlina yang terhapus (dibaca lewat API)

### TC-FA-SU-223: Penugasan paksa ke target Total Control, Read Only, Default User, atau akun sendiri

28. Ganti akun: login API sebagai Qori Akbar (Manage global user & role (Update), `Spectra.env.FA_MURG_UPD_PASSWORD`) untuk klien HTTP
29. Kirim permintaan langsung ke API assign grup Group Role `Manage files` pada General Affairs untuk Lina Marlina (Total Control) memakai klien HTTP dengan token sesi Qori Akbar
30. Verifikasi server menolak permintaan dengan status 403
31. Kirim permintaan langsung ke API assign grup Group Role `Manage files` pada General Affairs untuk Citra Lestari (Read Only) memakai klien HTTP dengan token sesi Qori Akbar
32. Verifikasi server menolak permintaan dengan status 403
33. Kirim permintaan langsung ke API assign grup Group Role `Manage files` pada General Affairs untuk Ahmad Dahlan (Default User) memakai klien HTTP dengan token sesi Qori Akbar
34. Verifikasi server menolak permintaan dengan status 403
35. Kirim permintaan langsung ke API assign grup Group Role `Manage files` pada General Affairs untuk Qori Akbar (akun sendiri) memakai klien HTTP dengan token sesi Qori Akbar
36. Verifikasi server menolak permintaan dengan status 403
37. Verifikasi tidak ada penugasan Group Role baru pada keempat target (dibaca lewat API)

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- K-1 dan bagian 8b butir 1: TC-FA-SU-222, 223, 272, dan 1062 (butir b) berformat Expected respons API (status respons dan state data). TC tetap masuk spec FE+BE walau tumpang tindih dengan pengujian tingkat endpoint; asersi spec hanya status respons dan state data, bukan tampilan UI.
- S-05: klausa "tidak ada entri log baru" pada TC-FA-SU-222, 223, dan 272 diasersi di spec 338 (kelas g) dengan permintaan yang sama sebagai pemicu, user dan baseline sendiri. Spec ini hanya mengasersi status respons dan state data; id TC tetap di `sourceTc` kedua spec.
- Urutan TC sumber diubah (TC-FA-SU-222, 272, 1062, 223) supaya aktor Manage user & role Group (Update) menyelesaikan semua blok sebelum ganti akun; langkah 18 mengulang blok tampilan dan permintaan TC-FA-SU-1062 untuk Group Manager (iterasi kedua mengulang langkah 9 sampai 17 dengan aktor Group Manager).
- Search untuk menemukan baris target (R-16) dicatat sebagai langkah penghubung.
- TC-FA-SU-1062 Expected a (UI) diasersi sebagai tampilan; Expected b (permintaan langsung) hanya status respons dan state data (bagian 8b butir 1).
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 9, 19.
- Ganti akun eksplisit (S-07): langkah 18, 28.
- Spec ini 37 langkah (di atas smell 35 langkah, dihitung dengan ekspansi). Alasan: seluruh blok satu kelas harness (defense-in-depth, kelas a) dan satu topik (penugasan Group Role dan Transaction Role yang ditolak), setiap blok berdiri sendiri dan hanya membaca; ekspansi berasal dari TC-FA-SU-1062 yang menuntut dua aktor dan TC-FA-SU-223 yang menuntut empat target.
- Temuan untuk QA:
  - TC-FA-SU-223 tidak menyebut Group Role dan grup yang di-assign; spec memakai `Manage files` pada General Affairs (sama dengan TC-FA-SU-968).
  - TC-FA-SU-272 tidak menyebut pengguna target dan baris yang di-remove; spec memakai Yuda Pratama (Pre-setup #39 memuat baris pada Logistics Warehouse).
  - TC-FA-SU-222 dan 223 tidak menyebut status respons selain 403 untuk kasus remove; spec mengikuti Expected.
  - Email dan password Qori Akbar (#4), Sinta Dewi (#6), dan Oscar Pranata (#9) tidak tertulis di Pre-setup TC; disediakan tim FE (S-11, S-13).
