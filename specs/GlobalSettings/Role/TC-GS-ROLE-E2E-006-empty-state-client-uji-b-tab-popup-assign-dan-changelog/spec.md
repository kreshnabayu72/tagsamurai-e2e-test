---
id: TC-GS-ROLE-E2E-006-empty-state-client-uji-b-tab-popup-assign-dan-changelog
title: "Empty State pada Client Uji B: Tab Read Only, Popup Assign, Modal Changelog, dan Tab Total Control yang Tidak Pernah Kosong"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-18
  - TC-GS-ROLE-20
  - TC-GS-ROLE-68
  - TC-GS-ROLE-198
coverage:
  web: automated
---

# Empty State pada Client Uji B: Tab Read Only, Popup Assign, Modal Changelog, dan Tab Total Control yang Tidak Pernah Kosong

## Prerequisites

- Mode: FE+BE.
- Aktor pertama (hook `before`): Total Control Client uji B (Pre-setup #14), email disediakan tim FE, password `Spectra.env.GS_CLIENTB_TC_PASSWORD`. Aktor kedua (langkah ganti akun 22): Ahmad Fauzi (Total Control client utama, Pre-setup #1), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Ahmad Fauzi). Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Role & Permission dengan Tab Total Control aktif pada Client uji B.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti hook suite (lihat `suite.md`), termasuk untuk akun Client uji B.
- Data Pre-setup Client uji B (#14): Default User (Budi Santoso) adalah satu-satunya Total Control dan satu-satunya pemegang baris "Import data"; tanpa user Read Only; tanpa riwayat Changelog Role & Permission; semua user ber-Access Global Settings sudah Total Control (kandidat Popup Assign kosong). Data Client uji B tidak diubah spec ini.
- Data client utama (TC-GS-ROLE-198 butir b): riwayat Changelog Tab Total Control tidak kosong; pencarian `zzqx` tidak cocok dengan entri mana pun.
- Spec hanya membaca data; tidak ada data yang dibuat, diubah, atau dihapus, sehingga tidak ada pemulihan Pre-setup.

## Test Steps

### TC-GS-ROLE-20: Tab Total Control dan Detail tidak pernah kosong

1. Verifikasi tabel Tab Total Control menampilkan tepat 1 baris `Budi Santoso` (Default User)
2. Verifikasi tidak ada empty state pada Tab Total Control
3. Klik Tab System
4. Klik Role Name `Import data`
5. Verifikasi Detail "Import data" menampilkan tepat 1 baris `Budi Santoso`

### TC-GS-ROLE-68: Empty state Popup Assign saat semua user eligible sudah di-assign

6. Klik segmen "System" pada breadcrumb
7. Klik Tab Total Control
8. Klik `[+ Assign]`
9. Verifikasi Popup Assign menampilkan Illustration
10. Verifikasi Popup Assign menampilkan Title "All eligible users have been assigned"
11. Verifikasi Popup Assign menampilkan Description "There are no additional eligible users available to select."
12. Klik `✕` pada header Popup Assign

### TC-GS-ROLE-18: Empty state Tab Read Only tanpa user Read Only

13. Klik Tab Read Only
14. Verifikasi area tabel menampilkan Illustration
15. Verifikasi area tabel menampilkan Title "No users assigned"
16. Verifikasi area tabel menampilkan Description "Users with read only access will appear here."

### TC-GS-ROLE-198: Empty state dan no-result Modal Changelog

17. Klik Changelog
18. Verifikasi Modal Changelog Tab Read Only menampilkan Illustration
19. Verifikasi Modal Changelog Tab Read Only menampilkan Title "No changelog yet"
20. Verifikasi Modal Changelog Tab Read Only menampilkan Description "Activities and changes will appear here."
21. Tutup Modal Changelog dengan `✕`
22. Logout, lalu login sebagai Total Control client utama (Ahmad Fauzi)
23. Buka Global Settings > Role & Permission (Tab Total Control)
24. Klik Changelog
25. Ketik Search `zzqx`, tekan Enter
26. Verifikasi Modal Changelog Tab Total Control menampilkan Illustration
27. Verifikasi Modal Changelog Tab Total Control menampilkan Title "No results found"
28. Verifikasi Modal Changelog Tab Total Control menampilkan Description "Try adjusting your search or filter."

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini kelas state tenant/data khusus (Client uji B, Pre-setup #14) dengan satu ganti akun eksplisit di langkah 22 hanya untuk butir b TC-GS-ROLE-198 (client utama, "Di client utama" pada langkah 2 TC). Bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3, ganti akun eksplisit).
- Urutan TC: TC-GS-ROLE-20 pertama karena tab awal Tab Total Control sudah termuat dan Detail "Import data" dibuka dari Tab System; TC-GS-ROLE-68 memakai kembali Tab Total Control; TC-GS-ROLE-18 dan butir a TC-GS-ROLE-198 memakai Tab Read Only yang sama; ganti akun ke client utama paling akhir. Perubahan urutan dari nomor TC mengurangi pembukaan ulang layar.
- Langkah penghubung (bukan dari TC sumber, tanpa `Verifikasi`): berpindah surface lewat breadcrumb dan tab (langkah 3, 6, 7, 13), menutup popup dan modal (langkah 12 dan 21), serta ganti akun dan membuka layar di client utama (langkah 22 dan 23).
- Post Condition TC-GS-ROLE-18, TC-GS-ROLE-20, TC-GS-ROLE-68, dan TC-GS-ROLE-198 kosong ("-"); tidak ada observasi tambahan.
- Temuan untuk QA:
  - TC-GS-ROLE-20 butir a ("1 baris Budi Santoso, tidak ada empty state") dan butir b tidak menyebut cara mengamati total baris selain jumlah baris tabel; spec mengasersi tepat satu baris tampil.
  - TC-GS-ROLE-198 langkah 2 menyebut "client utama" tanpa menyebut akun; spec memakai Ahmad Fauzi (Pre-setup #1).
