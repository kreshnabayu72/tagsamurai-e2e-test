---
id: TC-FA-GRP-E2E-060-edit-node-excess-node-menjadi-excess-saat-popup-terbuka-dan-node-dihapus-user-lain
title: "Edit pada Node Excess: Row Action Edit Hidden, Node Menjadi Excess Setelah Popup Dibuka, dan Node Dihapus User Lain Sebelum Save"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-187
  - TC-FA-GRP-188
  - TC-FA-GRP-189
coverage:
  web: automated
---

# Edit pada Node Excess: Row Action Edit Hidden, Node Menjadi Excess Setelah Popup Dibuka, dan Node Dihapus User Lain Sebelum Save

## Prerequisites

- Mode: FE+BE (backend nyata; kelas h state tenant: status Excess node akibat penurunan plan; TC-FA-GRP-188 memicu T-0 plan efektif).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Warehouse B (Assignable, Excess; TC-FA-GRP-187).
- Data Dinamis bersuffix `{runId}-060` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script): TC-FA-GRP-188: node `Excess Edit {runId}-060` (level 1, Description awal `Before Excess`, Description baru `After Excess`) menggantikan Branch Office Pre-setup supaya Pre-setup tidak berubah menjadi Excess (S-06). TC-FA-GRP-189: node `Stale Edit {runId}-060` (nama baru `Stale Edit Renamed {runId}-060`). Semua di-seed lewat API di hook `before`.
- State global yang diubah (kelas h): T-0 plan efektif membuat `Excess Edit {runId}-060` menjadi Excess (langkah 19). Pemicu T-0 (perubahan cap langsung atau hook uji handler plan efektif di lingkungan non-produksi), akun pelaku, dan pengembalian plan, cap, dan status Excess disediakan tim FE/BE (tidak disebut di TC, PRD, atau LLD). Hook `after` memulihkan plan, cap, dan status Excess walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: sesi API aktor untuk menghapus `Stale Edit {runId}-060` sebagai pelaku kedua (langkah 10); pembacaan status respons simpan (422) lewat intercept pasif atau fixture BE; pembacaan jumlah entri System Log dan Activity Log sebelum dan sesudah aksi (disediakan tim FE/BE; selisih terhadap baseline, S-12).
- Pemulihan (hook `after`): pulihkan plan, cap, dan status Excess; hapus lewat API node dengan suffix `{runId}-060`.

## Test Steps

### TC-FA-GRP-187: Row action Edit hidden pada node Excess (tabel dan sidebar)

1. Ketik Search `Warehouse B`, tekan Enter
2. Buka elipsis (⋯) baris Warehouse B di tabel
3. Verifikasi menu elipsis baris Warehouse B terbuka
4. Verifikasi Edit tidak dirender di tabel
5. Tutup menu elipsis (Esc) lalu buka elipsis (⋯) node Warehouse B di sidebar
6. Verifikasi menu elipsis node Warehouse B di sidebar terbuka
7. Verifikasi Edit tidak dirender di sidebar
8. Tutup menu elipsis (Esc)

### TC-FA-GRP-189: Node dihapus user lain sebelum Save (stale reference)

9. Ganti isi kotak Search dengan `Stale Edit {runId}-060`, tekan Enter
10. Buka elipsis (⋯) baris `Stale Edit {runId}-060`, lalu klik Edit (popup terbuka)
11. Lewat sesi API aktor, hapus `Stale Edit {runId}-060` hingga terhapus
12. Catat jumlah entri System Log dan Activity Log sebagai baseline (sesudah pelaku kedua selesai)
13. Ubah Group Name menjadi `Stale Edit Renamed {runId}-060`, lalu klik [Save]
14. Verifikasi popup ditutup
15. Verifikasi toast netral `This group is no longer available.`
16. Verifikasi tree di-refresh: `Stale Edit {runId}-060` tidak tampil di sidebar
17. Verifikasi tidak ada baris log baru: jumlah entri System Log dan Activity Log sama dengan baseline langkah 12
18. Klik `(←)` pada kotak Search

### TC-FA-GRP-188: Node jadi Excess setelah popup dibuka

19. Ketik Search `Excess Edit {runId}-060`, tekan Enter
20. Buka elipsis (⋯) baris `Excess Edit {runId}-060`, lalu klik Edit (popup terbuka)
21. Terapkan T-0 sehingga `Excess Edit {runId}-060` menjadi Excess (kemampuan tim FE/BE)
22. Ubah Description menjadi `After Excess`, lalu klik [Save]
23. Verifikasi server menolak dengan `422`
24. Verifikasi dialog `Group Is Read-Only` tampil di atas popup dengan isi `This group is now read-only because it's over your plan's group limit.` dan hanya tombol [OK]
25. Verifikasi tidak ada toast
26. Tekan Esc, lalu klik backdrop
27. Verifikasi dialog tetap tampil (Esc dan klik backdrop tidak menutup dialog)
28. Klik [OK]
29. Verifikasi dialog dan popup tertutup
30. Verifikasi tree di-refresh: `Excess Edit {runId}-060` tampil Excess (dim)
31. Verifikasi perubahan tidak tersimpan: Description `Excess Edit {runId}-060` tetap `Before Excess` (dibaca lewat fixture BE)
32. Pulihkan status Excess dan klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (backend nyata, kelas h state tenant; bagian 3 prinsip 13 butir h). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: TC-FA-GRP-187 dan TC-FA-GRP-189 (tanpa mengubah plan) lebih dulu, lalu TC-FA-GRP-188 yang memicu T-0 (S-10); berbeda dari urutan nomor TC sumber.
- Pelaku kedua pada TC-FA-GRP-189 memakai sesi API aktor (bukan konteks UI kedua), sehingga tanpa butir `P-2`.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 1 (Ketik Search `Warehouse B`, tekan Enter); langkah 5 (Tutup menu elipsis (Esc) lalu buka elipsis (⋯) node Warehouse B di sidebar); langkah 8 (Tutup menu elipsis (Esc)); langkah 9 (Ganti isi kotak Search dengan `Stale Edit {runId}-060`, tekan Enter); langkah 12 (Catat jumlah entri System Log dan Activity Log sebagai baseline sesudah pelaku kedua selesai dan tepat sebelum [Save], karena penghapusan oleh pelaku kedua sudah menambah entri log; S-12); langkah 18 (Klik `(←)` pada kotak Search); langkah 19 (Ketik Search `Excess Edit {runId}-060`, tekan Enter); langkah 21 (Terapkan T-0 sehingga `Excess Edit {runId}-060` menjadi Excess, kemampuan tim FE/BE); langkah 32 (Pulihkan status Excess dan klik `(←)` pada kotak Search).
- Pencarian baris target (S-03, R-16): langkah 1 (Ketik Search `Warehouse B`, tekan Enter) menemukan baris target; client memiliki lebih dari 10 node level 1 dan page size 10, jadi baris target tidak dijamin berada di halaman 1 All Groups.
- Asersi "tidak ada baris log baru" TC-FA-GRP-189 ditulis sebagai `Verifikasi` berbaseline jumlah entri di spec ini (S-12) dengan toast netral sebagai anchor respons server; Changelog node tidak dibaca karena node sudah terhapus.
- Asersi absence "Edit tidak dirender" didahului `Verifikasi` menu elipsis terbuka sebagai anchor permukaan (8b butir 2).
- Temuan untuk QA:
  - TC-FA-GRP-188 menyebut Branch Office (Pre-setup); spec memakai node milik spec yang dijadikan Excess supaya Pre-setup tidak berubah.
  - TC-FA-GRP-188 tidak menyebut pelaku dan mekanisme T-0 / penurunan plan; dicatat sebagai kemampuan "disediakan tim FE/BE".
  - TC-FA-GRP-188 Expected c "Perubahan tidak tersimpan" tidak menyebut cara membaca; spec memakai pembacaan nilai Description lewat fixture BE.
  - TC-FA-GRP-189 Expected a "tree di-refresh" tidak menyebut apa yang teramati; spec mengasersi `Stale Edit` tidak lagi tampil di sidebar.
  - TC-FA-GRP-187 tidak menyebut isi menu elipsis node Excess selain Edit yang tidak dirender; spec memakai menu terbuka sebagai anchor.

