---
name: tagsamurai-e2e-generate-spec
description: Workflow untuk menurunkan TC granular (tc-[modul].md) menjadi spec.md e2e TestSpectra untuk satu submodul TAG Samurai. Dipakai saat membuat suite baru atau menambah spec e2e dari TC granular.
---

# Generate Spec E2E dari TC Granular

Aturan lengkap ada di `docs/e2e-conventions.md`. Baca bagian yang ditunjuk "Peta baca per peran" di awal dokumen itu, lalu ikuti alur ini. Konvensi dan skill ini beku selama run (bagian 11): catat sha256 `docs/e2e-conventions.md`, skill ini, dan TC sumber di awal run dan cocokkan lagi sebelum laporan akhir; bila berubah, berhenti dan laporkan. Skill framework `spec-and-suite-authoring` dan `workspace-structure` tetap berlaku.

## Input yang wajib ada

1. Path `tc-[modul].md` (TC granular) dan kalau ada `tc-[modul]-backend.md` (untuk mengenali TC hanya-BE).
2. Kode prefix modul dari `foundation/tc-prefix-registry.md` (contoh `GS` + `USER`).
3. Cakupan yang diminta (seluruh submodul, satu section, atau daftar TC).

Kalau salah satu tidak ada, berhenti dan tanyakan. Jangan menebak prefix.

## Langkah

1. **Baca TC sumber** sampai tabel Data Uji Pre-setup dan Data Uji Dinamis, bukan hanya baris TC-nya.
2. **Seleksi** dengan bagian 2 konvensi: semua TC masuk spec kecuali yang hanya-BE. Kasus hanya-FE (tampilan murni, tooltip, Setup Column, hover, keystroke, kegagalan server) tetap masuk sebagai spec dengan `Mode: mock` di `## Prerequisites`; kasus yang memukul backend nyata masuk sebagai spec FE+BE. Spec yang memakai intercept parsial di atas backend nyata atau mengasersi state backend ditandai FE+BE, bukan mock (bagian 6 konvensi). Hambatan teknis dan label "Manual" bukan alasan mengeluarkan TC: tulis semua kebutuhan (data, akun, waktu, kuota, race, pemicu kegagalan, kemampuan teknis) di `## Prerequisites` sebagai sumber resmi bagi tim FE. `## Notes` hanya penjelasan tambahan. Buat daftar TC yang masuk dan yang hanya-BE.
3. **Kelompokkan** sesuai prinsip bagian 3 konvensi: satu spec = satu topik aksi yang bisa dijalankan berurutan, screening di awal, validasi yang diblokir sebelum aksi sukses, aksi yang menghapus data di akhir, kasus menutup form di akhir, variasi topik yang sama berurutan. Pisahkan topik aksi berbeda yang butuh kondisi data bervariasi (Delete, Toggle Active, Remove Access), beda entity, bergantung hardware, atau pembuat data yang perlu dipisah dari yang tidak. Kasus blokir karena kondisi data target (bukan validasi field dan bukan blokir identitas atau role) dijadikan spec sendiri per topik (prinsip 12). Beri tiap TC label kelas harness (prinsip 13: defense-in-depth, fault injection, multi-konteks, harness eksternal, volume data, binary buffer, absence log, state tenant) dan jangan taruh TC berkelas harness di spec screening atau fungsional biasa; satu spec = satu kelas. Kelas ringan (defense-in-depth tanpa harness eksternal, fault injection) cukup satu spec per kelas per modul, bukan per aksi; kelas berat (multi-konteks, harness eksternal, volume data) satu spec per jenis harness. Spec yang diperkirakan melewati sekitar 35 langkah atau memuat lebih dari satu kelas ditinjau ulang sebelum rencana diajukan. Spec yang tetap di atas 35 langkah wajib punya alasan di `## Notes` (jangan dikarang; kalau tidak ada alasan, pecah). Kasus tanpa submit (checklist, batas panjang, validasi inline) memakai satu pembukaan link dengan field dikosongkan di antara kasus, bukan satu user dan satu pembukaan per TC. Kasus izin per role mengikuti bagian 3a (Role Matrix): spec positif dan negatif per aksi, satu spec untuk banyak role. Catat data mana yang harus dibuat sendiri per spec (bagian 5) dan berapa kali form dibuka.
4. **Tampilkan rencana ke user dan tunggu persetujuan** sebelum menulis file. Rencana berisi tabel:
   `spec (id + judul)` | `sourceTc` | `role/precondition` | `data` | `hook/step yang dibutuhkan` | `kelas harness` | `jumlah langkah (perkiraan)` | `mode (FE+BE / mock)` | `TC hanya-BE`.
5. Setelah disetujui, buat di `specs/<ModulBesar>/<SubModul>/` (PascalCase, contoh `specs/GlobalSettings/User/`):
   - `suite.md` hanya jika belum ada (`id: suite-<kebab>`, `parallel: true` hanya jika semua spec independen). Kalau sudah ada, pakai apa adanya.
   - `TC-<ModulBesar>-<SubModul>-E2E-<NNN>-<slug>/spec.md`, dengan `NNN` melanjutkan nomor terakhir di suite itu.
6. Isi frontmatter sesuai bagian 8 konvensi, termasuk `sourceTc` (daftar id TC granular) dan `status: draft`. `caseType` spec gabungan ikut jenis alur utama yang dominan (bagian 8 konvensi). `coverage.web: automated` untuk spec yang dirancang untuk otomasi, progres dibaca dari `status`.
7. **Tulis body spec.md** mengikuti konvensi bagian 5 sampai 9, 10, 10a, dan butir Lampiran A modul ini (aturan lengkapnya ada di sana, tidak diulang di skill ini). Struktur wajib:
   - Bahasa Indonesia dengan teks UI persis seperti di aplikasi; slug `id` dan folder bahasa Indonesia (bagian 7).
   - `# <title>` sama dengan `title`.
   - `## Prerequisites`: butir pertama baris `Mode:` (R-01), lalu akun, env, data Pre-setup dan Dinamis, hook, kemampuan teknis, dan state global beserta pemulihannya (S-11). Untuk spec Role Matrix, tabel "Role yang diuji" (bagian 3a).
   - `## Test Steps`: langkah bernomor, konkret, satu aksi per baris (langkah berulang ditulis sebagai teks biasa), subjudul `###` untuk spec panjang (bagian 3). Jangan menulis `@step:<nama>` (bagian 8a): `@step` ditambahkan skill `tagsamurai-e2e-generate-script` saat Step-nya dibuat. Expected menjadi langkah `Verifikasi` tepat setelah aksinya (R-03).
   - Pola berulang yang wajib dihindari saat menulis (juga diperiksa audit):
     - Asersi yang merujuk "baseline sesudah TC-xxx" atau "bertambah dari" didahului langkah `Catat ...` (bukan `Verifikasi`) tepat setelah write TC itu; N total surface audit-trail bersama dibaca via BE sebelum aksi (8b.10, S-12).
     - Beri langkah `Tunggu aksi selesai` setelah Submit/Confirm/Delete yang hasilnya tidak diasersi dan sebelum ganti surface/akun/sesi atau membuka log.
     - Tutup modal Event Log sebelum pindah ke surface berikutnya (hook `afterEach` tidak jalan antar-iterasi dalam satu `it()`).
     - `## Prerequisites` hanya memuat yang dipakai langkah: tanpa kunci fixture tak terpakai, tanpa frasa "tahap script", tanpa penanda rencana Q-n/D-n. Langkah memakai kunci `Fixture.tagStock.<key>`, bukan literal Pre-setup mentah (kecuali nilai Expected dan nama file).
     - Jangan tulis "Kesamaan akun dikonfirmasi tim FE"; tulis "perlu dikonfirmasi tim FE".
     - Asersi absence/universal didahului anchor positif ("sedikitnya satu baris").
     - Search yang nilainya bertahan setelah breadcrumb/Back: tulis "ganti isi kotak search dengan X" (8b.9).
   - `## Notes`: langkah penghubung, penyimpangan urutan, pembagian TC lintas spec, id pengecualian (`P-n`, `K-1`), dan "Temuan untuk QA" (S-03, S-05, S-15), ditulis sebagai keadaan final (bagian 7).
8. **Swa-periksa** tiap spec terhadap konvensi bagian 10 (S-01 sampai S-15), bagian 10a (R-01 sampai R-21), dan butir Lampiran A modul ini sebelum lint. Audit memakai daftar dan id yang sama, jadi butir yang lolos di sini tidak menjadi temuan audit. Butir bertanda kode C di bagian 10a diperiksa `check-suite.py` di langkah 9 dan tidak perlu ditelusuri manual per spec; periksa manual butir tanpa kode C.
9. Jalankan `spectra lint --strict specs/<Suite>` dan `python scripts/check-suite.py specs/<Suite> <path tc-[modul].md> docs/coverage/<Suite>.md`; perbaiki semua [FINDING] sampai bersih dan baca tiap [REVIEW]. [FINDING] C11 sampai C18 bersifat mekanis: perbaiki teks yang ditunjuk tanpa menelusuri ulang aturannya.
10. Update `docs/coverage/<Suite>.md`: pemetaan TC granular ke spec, alasan TC hanya-BE, dan tabel "Lapisan per TC" (Spec, Mode).
11. Laporkan ke user: daftar spec, TC yang dilewati, temuan TC sumber (ambigu, kontradiktif, precondition kurang; S-15), dan hal yang butuh keputusan. Jangan lanjut membuat `web.test.ts`, itu skill `tagsamurai-e2e-generate-script`.

## Larangan

- Jangan mengubah isi atau nomor TC granular. Kalau menemukan masalah di TC sumber, catat sebagai temuan untuk QA.
- Jangan merenumber id spec yang sudah ada.
- Jangan mengubah `ARCHITECTURE.md`, `spectra.config.ts`, `package.json`, atau spec suite lain tanpa izin.
- Jangan menyimpan password atau token di spec dan fixture.
- Jangan membuat spec yang bergantung pada hasil spec lain.
